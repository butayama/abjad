from abjad.tools import contexttools
from abjad.tools import durationtools
from abjad.tools.abctools import AbjadObject


class QTargetBeat(AbjadObject):
    '''Representation of a single "beat" in a quantization target:

    ::

        >>> beatspan = (1, 8)
        >>> offset_in_ms = 1500
        >>> search_tree = quantizationtools.SimpleSearchTree({3: None})
        >>> tempo = contexttools.TempoMark((1, 4), 56)

    ::

        >>> q_target_beat = quantizationtools.QTargetBeat(
        ...     beatspan=beatspan,
        ...     offset_in_ms=offset_in_ms,
        ...     search_tree=search_tree,
        ...     tempo=tempo,
        ...     )

    ::

        >>> q_target_beat
        quantizationtools.QTargetBeat(
            beatspan=durationtools.Duration(1, 8),
            offset_in_ms=durationtools.Offset(1500, 1),
            search_tree=quantizationtools.SimpleSearchTree(
                definition={   3: None}
                ),
            tempo=contexttools.TempoMark(
                durationtools.Duration(1, 4),
                56
                )
            )

    Not composer-safe.

    Used internally by quantizationtools.Quantizer.

    Return ``QTargetBeat`` instance.
    '''

    ### CLASS ATTRIBUTES ###

    __slots__ = ('_beatspan', '_distances', '_grouping', '_offset_in_ms',
        '_q_events', '_q_grid', '_q_grids', '_search_tree', '_tempo')

    ### INITIALIZER ###

    def __init__(self, beatspan=None, offset_in_ms=None, search_tree=None, tempo=None):
        from experimental import quantizationtools

        beatspan = durationtools.Duration(beatspan)
        offset_in_ms = durationtools.Offset(offset_in_ms)

        if search_tree is None:
            search_tree = quantizationtools.SimpleSearchTree()
        assert isinstance(search_tree, quantizationtools.SearchTree)
        tempo = contexttools.TempoMark(tempo)
        assert not tempo.is_imprecise

        q_events = []
        q_grids = []
        
        self._beatspan = beatspan
        self._distances = {}
        self._offset_in_ms = offset_in_ms
        self._q_events = q_events
        self._q_grid = None
        self._q_grids = q_grids
        self._search_tree = search_tree
        self._tempo = tempo

    ### SPECIAL METHODS ###

    def __call__(self, job_id):
        from experimental import quantizationtools
        if not self.q_events:
            return None
        assert all([isinstance(x, quantizationtools.QEvent) for x in self.q_events])
        q_event_proxies = []
        for q_event in self.q_events:
            q_event_proxy = quantizationtools.QEventProxy(
                q_event, self.offset_in_ms, self.offset_in_ms + self.duration_in_ms)
            q_event_proxies.append(q_event_proxy)
        return quantizationtools.QuantizationJob(job_id, self.search_tree, q_event_proxies)

    def __repr__(self):
        return self._tools_package_qualified_indented_repr

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def beatspan(self):
        '''The beatspan of the ``QTargetBeat``:

        ::

            >>> q_target_beat.beatspan
            Duration(1, 8)

        Return Duration.
        '''
        return self._beatspan

    @property
    def distances(self):
        '''A list of computed distances between the ``QEventProxies``
        associated with a ``QTargetBeat`` instance, and each ``QGrid``
        generated for that beat.

        Used internally by the ``Quantizer``.

        Return tuple.
        '''
        return self._distances

    @property
    def duration_in_ms(self):
        '''The duration in milliseconds of the ``QTargetBeat``:

        ::

            >>> q_target_beat.duration_in_ms
            Duration(3750, 7)

        Return Duration instance.
        '''
        from experimental import quantizationtools
        return quantizationtools.tempo_scaled_rational_to_milliseconds(
            self.beatspan, self.tempo)

    @property
    def offset_in_ms(self):
        '''The offset in milliseconds of the ``QTargetBeat``:

        ::

            >>> q_target_beat.offset_in_ms
            Offset(1500, 1)

        Return Offset instance.
        '''
        return self._offset_in_ms

    @property
    def q_events(self):
        '''A list for storing ``QEventProxy`` instances.

        Used internally by the ``Quantizer``.

        Return list.
        '''
        return self._q_events

    @property
    def q_grid(self):
        '''The ``QGrid`` instance selected by a ``Heuristic``.

        Used internally by the ``Quantizer``.

        Return ``QGrid`` instance.
        '''
        return self._q_grid
    
    @property
    def q_grids(self):
        '''A tuple of ``QGrids`` generated by a ``QuantizationJob``.

        Used internally by the ``Quantizer``.

        Return tuple.
        '''
        return self._q_grids

    @property
    def search_tree(self):
        '''The search tree of the ``QTargetBeat``:

        ::

            >>> q_target_beat.search_tree
            SimpleSearchTree(
                definition={   3: None}
                )

        Return ``SearchTree`` instance.
        '''
        return self._search_tree

    @property
    def tempo(self):
        '''The tempo of the ``QTargetBeat``:

        ::

            >>> q_target_beat.tempo
            TempoMark(Duration(1, 4), 56)

        Return ``TempoMark`` instance.
        '''
        return self._tempo
