from abjad import *


def test_divide_tie_chain_into_arbitrary_diminution_dotted_01( ):

   t = Staff([Note(0, (1, 8)), Note(0, (1, 16)), Note(0, (1, 16))])
   Tie(t[:2])
   Beam(t[:])

   r'''
   \new Staff {
           c'8 [ ~
           c'16
           c'16 ]
   }
   '''

   divide.tie_chain_into_arbitrary_diminution_dotted(t[0].tie.chain, [1])

   r'''
   \new Staff {
           {
                   c'8. [
           }
           c'16 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\t{\n\t\tc'8. [\n\t}\n\tc'16 ]\n}"


def test_divide_tie_chain_into_arbitrary_diminution_dotted_02( ):

   t = Staff([Note(0, (1, 8)), Note(0, (1, 16)), Note(0, (1, 16))])
   Tie(t[:2])
   Beam(t[:])
   divide.tie_chain_into_arbitrary_diminution_dotted(t[0].tie.chain, [1, 2])

   r'''
   \new Staff {
           {
                   c'16
                   c'8
           }
           c'16 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\t{\n\t\tc'16 [\n\t\tc'8\n\t}\n\tc'16 ]\n}"


def test_divide_tie_chain_into_arbitrary_diminution_dotted_03( ):

   t = Staff([Note(0, (1, 8)), Note(0, (1, 16)), Note(0, (1, 16))])
   Tie(t[:2])
   Beam(t[:])
   divide.tie_chain_into_arbitrary_diminution_dotted(
      t[0].tie.chain, [1, 2, 2])

   r'''
   \new Staff {
           \times 4/5 {
                   c'32. [
                   c'16.
                   c'16.
           }
           c'16 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Staff {\n\t\\times 4/5 {\n\t\tc'32. [\n\t\tc'16.\n\t\tc'16.\n\t}\n\tc'16 ]\n}"
