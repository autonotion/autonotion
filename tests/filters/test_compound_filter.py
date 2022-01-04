import pytest
from autonotion.filters import compound
from autonotion.filters.compound import CompoundFilter
from autonotion.filters.database import TextNotionFilter

@pytest.fixture
def text_filter():
    return TextNotionFilter(property="name", equals="John")


def test_compound_filter_and_initialization(text_filter):
    
    compound_filter = CompoundFilter(
        and_=[text_filter],
    )
    
    assert compound_filter.dict() == {
        'and': [
            {
                'property': 'name',
                'text': {
                    'equals': 'John'
                }
            }
        ]
    }


def test_compound_filter_or_initialization(text_filter):
        
        compound_filter = CompoundFilter(
            or_=[text_filter],
        )
        
        assert compound_filter.dict() == {
            'or': [
                {
                    'property': 'name',
                    'text': {
                        'equals': 'John'
                    }
                }
            ]
        }


def test_compound_filter_and_or_initialization_fails(text_filter):
    with pytest.raises(ValueError):
        CompoundFilter(
            and_=[text_filter],
            or_=[text_filter],
        )

