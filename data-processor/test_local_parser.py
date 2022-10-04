import local_parser


def test_composite():
    assert local_parser.it_is_composite(24, 72) == 0

def test_lists():
    assert local_parser.know_list_len(l1=[2,3,4], l2=[4,5,6]).equals(list)
