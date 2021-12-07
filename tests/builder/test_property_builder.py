import datetime
import json
from autonotion.models.blocks import TextBlock, Annotation
from autonotion.models.builder import PropertyBuilder
from autonotion.models.properties import (
    CreatedTime,
    Date,
    DateProperty,
    Formula,
    FormulaProperty,
    MultiSelectProperty,
    People,
    PeopleProperty,
    SelectOption,
    SelectProperty,
    TitleProperty
)


def test_property_builder_should_be_able_to_build_formula():
    expected = FormulaProperty(
        type='formula',
        id='id',
        name='Formula 1',
        formula=Formula(
            type='string',
            string='15/12/21 00:00'
        )
    )
    formula = json.loads("""
        {
            "id": "id",
            "type": "formula",
            "formula": {
                "type": "string",
                "string": "15/12/21 00:00"
            }
        }
    """)
    assert PropertyBuilder.build('Formula 1', formula) == expected


def test_property_builder_should_be_able_to_build_multiselect():
    expected = MultiSelectProperty(
        id='id',
        type='multi_select',
        name="Labels",
        multi_select=[
            SelectOption(
                id='id',
                name='notion',
                color='purple'
            ),
            SelectOption(
                id='id',
                name='twitter',
                color='blue'
            ),
            SelectOption(
                id='id',
                name='facebook',
                color='blue'
            )
        ]
    )

    multiselect = json.loads("""
        {
            "id": "id",
            "type": "multi_select",
            "multi_select": [
                {
                    "id": "id",
                    "name": "notion",
                    "color": "purple"
                },
                {
                    "id": "id",
                    "name": "twitter",
                    "color": "blue"
                },
                {
                    "id": "id",
                    "name": "facebook",
                    "color": "blue"
                }
            ]
        }
    """)

    assert PropertyBuilder.build('Labels', multiselect) == expected


def test_property_builder_should_be_able_to_build_creation_time():
    expected = CreatedTime(
        name="Created time",
        id="id",
        type="created_time",
        created_time=datetime.datetime(2021, 12, 6, 17, 41, 00, tzinfo=datetime.timezone.utc)
    )
    creation_time = json.loads("""
        {
            "id": "id",
            "type": "created_time",
            "created_time": "2021-12-06T17:41:00.000Z"
        }
    """)
    assert PropertyBuilder.build('Created time', creation_time) == expected


def test_property_builder_should_be_able_to_build_people_property():
    expected = PeopleProperty(
        type='people',
        id='id',
        name='Assign',
        people=[
            People(
                id='id',
                name='John Doe',
                avatar_url='https://gravatar.com/avatar/',
                person={
                    'email': 'jondoe@autonotion.com'
                }
            )
        ]
    )
    people = json.loads("""
        {
            "id": "id",
            "type": "people",
            "people": [
                {
                    "object": "user",
                    "id": "id",
                    "name": "John Doe",
                    "avatar_url": "https://gravatar.com/avatar/",
                    "type": "person",
                    "person": {
                        "email": "jondoe@autonotion.com"
                    }
                }
            ]
        }
        """)
    assert PropertyBuilder.build('Assign', people) == expected


def test_property_builder_should_be_able_to_build_select_property():
    expected = SelectProperty(
        id='id',
        type='select',
        name='Status',
        select=SelectOption(
            id='id',
            name='Not started',
            color='red',
        )
    )

    select = json.loads("""
        {
            "id": "id",
            "type": "select",
            "select": {
                "id": "id",
                "name": "Not started",
                "color": "red"
            }
        }
    """)

    assert PropertyBuilder.build('Status', select) == expected


def test_property_builder_should_build_date_property():
    expected = DateProperty(
        id='id',
        name='Due date',
        type='date',
        date=Date(
            start=datetime.date(2021, 12, 15),
            end=None
        )
    )

    date = json.loads("""
        {
                "id": "id",
                "type": "date",
                "date": {
                    "start": "2021-12-15",
                    "end": null
                }
            }
    """)

    assert PropertyBuilder.build('Due date', date) == expected


def test_property_builder_should_build_title_property():
    expected = TitleProperty(
        id='title',  # It's always title in API repsonse
        name='Name',  # It's always Name in API response
        type='title',
        title=[
            TextBlock(
                type='text',
                annotations=Annotation(),
                plain_text="This is a test for integration library for Notion API",
                href=None
            )
        ]
    )

    title = json.loads("""
        {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "This is a test for integration library for Notion API",
                        "link": null
                    },
                    "annotations": {
                        "bold": false,
                        "italic": false,
                        "strikethrough": false,
                        "underline": false,
                        "code": false,
                        "color": "default"
                    },
                    "plain_text": "This is a test for integration library for Notion API",
                    "href": null
                }
            ]
        }""")

    assert PropertyBuilder.build('Name', title) == expected
