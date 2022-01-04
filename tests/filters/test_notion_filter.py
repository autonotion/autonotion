import pytest
from datetime import datetime
from autonotion.filters import (
    TextNotionFilter,
    NumberNotionFilter,
    SelectNotionFilter,
    MultiSelectNotionFilter,
    CheckboxNotionFilter,
    DateTimeNotionFilter,
    PersonNotionFilter,
    FileNotionFilter,
    FormulaNotionFilter
)

@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'text', 'equals': 'test'}, TextNotionFilter(property='text', equals='test')),
    ({'property': 'text', 'does_not_equal': 'test'}, TextNotionFilter(property='text', does_not_equal='test')),
    ({'property': 'text', 'contains': 'test'}, TextNotionFilter(property='text', contains='test')),
    ({'property': 'text', 'starts_with': 'test'}, TextNotionFilter(property='text', starts_with='test')),
    ({'property': 'text', 'ends_with': 'test'}, TextNotionFilter(property='text', ends_with='test')),
    ({'property': 'text', 'is_empty': True}, TextNotionFilter(property='text', is_empty=True)),
    ({'property': 'text', 'is_not_empty': True}, TextNotionFilter(property='text', is_not_empty=True)),
])
def test_text_notion_filter_initialization(init_values, expected):
    assert TextNotionFilter(**init_values) == expected


@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'number', 'equals': 1}, NumberNotionFilter(property='number', equals=1)),
    ({'property': 'number', 'does_not_equal': 1.0}, NumberNotionFilter(property='number', does_not_equal=1.0)),
    ({'property': 'number', 'greater_than': 1}, NumberNotionFilter(property='number', greater_than=1)),
    ({'property': 'number', 'greater_than_or_equal': -1.0}, NumberNotionFilter(property='number', greater_than_or_equal=-1.0)),
    ({'property': 'number', 'less_than': -1}, NumberNotionFilter(property='number', less_than=-1)),
    ({'property': 'number', 'less_than_or_equal': 1}, NumberNotionFilter(property='number', less_than_or_equal=1)),
    ({'property': 'number', 'is_empty': True}, NumberNotionFilter(property='number', is_empty=True)),
    ({'property': 'number', 'is_not_empty': False}, NumberNotionFilter(property='number', is_not_empty=False)),
])
def test_number_notion_filter_initialization(init_values, expected):
    assert NumberNotionFilter(**init_values) == expected


@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'checkbox', 'equals': True}, CheckboxNotionFilter(property='checkbox', equals=True)),
    ({'property': 'checkbox', 'does_not_equal': False}, CheckboxNotionFilter(property='checkbox', does_not_equal=False)),
])
def test_checkbox_notion_filter_initialization(init_values, expected):
    assert CheckboxNotionFilter(**init_values) == expected


@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'select', 'equals': 'test'}, SelectNotionFilter(property='select', equals='test')),
    ({'property': 'select', 'does_not_equal': 'test'}, SelectNotionFilter(property='select', does_not_equal='test')),
    ({'property': 'select', 'is_empty': True}, SelectNotionFilter(property='select', is_empty=True)),
    ({'property': 'select', 'is_not_empty': True}, SelectNotionFilter(property='select', is_not_empty=True)),
])
def test_select_notion_filter_initialization(init_values, expected):
    assert SelectNotionFilter(**init_values) == expected


@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'multiselect', 'contains': 'test'}, MultiSelectNotionFilter(property='multiselect', contains='test')),
    ({'property': 'multiselect', 'does_not_contain': 'test'}, MultiSelectNotionFilter(property='multiselect', does_not_contain='test')),
    ({'property': 'multiselect', 'is_empty': True}, MultiSelectNotionFilter(property='multiselect', is_empty=True)),
    ({'property': 'multiselect', 'is_not_empty': True}, MultiSelectNotionFilter(property='multiselect', is_not_empty=True)),
])
def test_multiselect_notion_filter_initialization(init_values, expected):
    assert MultiSelectNotionFilter(**init_values) == expected


now = datetime.now()

@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'datetime', 'equals': now}, DateTimeNotionFilter(property='datetime', equals=now)),
    ({'property': 'datetime', 'before': now}, DateTimeNotionFilter(property='datetime', before=now)),
    ({'property': 'datetime', 'after': now}, DateTimeNotionFilter(property='datetime', after=now)),
    ({'property': 'datetime', 'on_or_before': now}, DateTimeNotionFilter(property='datetime', on_or_before=now)),
    ({'property': 'datetime', 'on_or_after': now}, DateTimeNotionFilter(property='datetime', on_or_after=now)),
    ({'property': 'datetime', 'is_empty': True}, DateTimeNotionFilter(property='datetime', is_empty=True)),
    ({'property': 'datetime', 'is_not_empty': True}, DateTimeNotionFilter(property='datetime', is_not_empty=True)),
    ({'property': 'datetime', 'past_week': True}, DateTimeNotionFilter(property='datetime', past_week=True)),
    ({'property': 'datetime', 'past_month': True}, DateTimeNotionFilter(property='datetime', past_month=True)),
    ({'property': 'datetime', 'past_year': True}, DateTimeNotionFilter(property='datetime', past_year=True)),
    ({'property': 'datetime', 'next_week': True}, DateTimeNotionFilter(property='datetime', next_week=True)),
    ({'property': 'datetime', 'next_month': True}, DateTimeNotionFilter(property='datetime', next_month=True)),
    ({'property': 'datetime', 'next_year': True}, DateTimeNotionFilter(property='datetime', next_year=True)),

])
def test_datetime_notion_filter_initialization(init_values, expected):
    assert DateTimeNotionFilter(**init_values) == expected


@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'person', 'contains': 'UUID4'}, PersonNotionFilter(property='person', contains='UUID4')),
    ({'property': 'person', 'does_not_contain': 'UUID4'}, PersonNotionFilter(property='person', does_not_contain='UUID4')),
    ({'property': 'person', 'is_empty': True}, PersonNotionFilter(property='person', is_empty=True)),
    ({'property': 'person', 'is_not_empty': True}, PersonNotionFilter(property='person', is_not_empty=True)),
])
def test_person_notion_filter_initialization(init_values, expected):
    assert PersonNotionFilter(**init_values) == expected


@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'file', 'is_empty': True}, FileNotionFilter(property='file', is_empty=True)),
    ({'property': 'file', 'is_not_empty': True}, FileNotionFilter(property='file', is_not_empty=True)),
])
def test_file_notion_filter_initialization(init_values, expected):
    assert FileNotionFilter(**init_values) == expected


@pytest.mark.parametrize("init_values, expected", [
    ({'property': 'formula', 'text': 'test'}, FormulaNotionFilter(property='formula', text='test')),
    ({'property': 'formula', 'checkbox': True}, FormulaNotionFilter(property='formula', checkbox=True)),
    ({'property': 'formula', 'number': 1}, FormulaNotionFilter(property='formula', number=1)),
    ({'property': 'formula', 'number': 1.0}, FormulaNotionFilter(property='formula', number=1.0)),
    ({'property': 'formula', 'date': now}, FormulaNotionFilter(property='formula', date=now)),
])
def test_formula_notion_filter_initialization(init_values, expected):
    assert FormulaNotionFilter(**init_values) == expected


@pytest.mark.parametrize("filter, property", [
    (DateTimeNotionFilter(property='date', past_week=True), 'past_week'),
    (DateTimeNotionFilter(property='date', past_month=True), 'past_month'),
    (DateTimeNotionFilter(property='date', past_year=True), 'past_year'),
    (DateTimeNotionFilter(property='date', next_week=True), 'next_week'),
    (DateTimeNotionFilter(property='date', next_month=True), 'next_month'),
    (DateTimeNotionFilter(property='date', next_year=True), 'next_year'),
])
def test_dict_convert_translation_field_in_datetime_filter(filter, property):
    assert filter.dict().get('datetime').get(property) == {}
