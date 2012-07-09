from experimental.selectortools.BackgroundElementSliceSelector import BackgroundElementSliceSelector


class MultipleContextDivisionSliceSelector(BackgroundElementSliceSelector):
    r'''.. versionadded:: 1.0

    ::

        >>> from experimental import selectortools
        >>> from experimental import timespantools

    Select the first five divisions starting in segment ``'red'``.
    Do this in both ``'Voice 1'`` and ``'Voice 3'``::

        >>> segment_selector = selectortools.SegmentSelector(index='red')
        >>> inequality = timespantools.expr_starts_during_timespan(segment_selector.timespan)
        >>> division_selector = selectortools.MultipleContextDivisionSliceSelector(
        ... contexts=['Voice 1', 'Voice 3'], inequality=inequality, stop=5)

    ::

        >>> z(division_selector)
        selectortools.MultipleContextDivisionSliceSelector(
            contexts=['Voice 1', 'Voice 3'],
            inequality=timespantools.TimespanInequality(
                timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                timespantools.SingleSourceTimespan(
                    selector=selectortools.SegmentSelector(
                        index='red'
                        )
                    )
                ),
            stop=5
            )

    ``MultipleContextDivisionSliceSelector`` properties are read-only.
    '''

    ### INITIALIZER ###

    def __init__(self, contexts=None, inequality=None, start=None, stop=None):
        from experimental import specificationtools
        BackgroundElementSliceSelector.__init__(self, specificationtools.Division,
            inequality=inequality, start=start, stop=stop)
        assert isinstance(contexts, (list, type(None))), repr(contexts)
        contexts = self._process_contexts(contexts)
        self._contexts = contexts

    ### PRIVATE METHODS ###

    def _process_contexts(self, contexts):
        from experimental import specificationtools
        if contexts is None:
            return contexts
        result = []
        for context in contexts:
            component_name = specificationtools.expr_to_component_name(context)
            result.append(component_name)
        return result

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def contexts(self):
        return self._contexts
