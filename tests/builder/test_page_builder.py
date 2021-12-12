import json
from datetime import datetime, timezone, date
from autonotion.models.builder import PageBuilder
from autonotion.models.pages import DatabaseParent, Page
from autonotion.models.blocks import TextBlock, TextBlockContent, Annotation

from autonotion.models.properties import (
    CreatedTime,
    Date,
    DateProperty,
    Formula,
    FormulaPropertyInstance,
    MultiSelectProperty,
    People,
    PeopleProperty,
    SelectOption,
    SelectProperty,
    TitleProperty
)


def test_page_builder_will_create_page_from_api_response(page):
    raw_data = json.loads(page)

    expected_page = Page(
        object='page',
        id='id',
        created_time=datetime(2021, 12, 6, 17, 41, 0, tzinfo=timezone.utc),
        last_edited_time=datetime(2021, 12, 6, 19, 12, 0, tzinfo=timezone.utc),
        archived=False,
        icon=None,
        # cover=None,
        parent=DatabaseParent(
            type='database_id',
            database_id='id'
        ),
        properties=[
            FormulaPropertyInstance(
                type='formula',
                id='id',
                name='Formula 1',
                formula=Formula(
                    type='string',
                    string='15/12/21 00:00'
                )
            ),
            MultiSelectProperty(
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
            ),
            CreatedTime(
                name="Created time",
                id="id",
                type="created_time",
                created_time=datetime(2021, 12, 6, 17, 41, 00, tzinfo=timezone.utc)
            ),
            PeopleProperty(
                type='people',
                id='id',
                name='Assign',
                people=[
                    People(
                        id='id',
                        name='John Doe',
                        avatar_url='https://gravatar.com/avatar/',
                        person={
                            'email': 'jhondoe@autonotion.com'
                        }
                    )
                ]
            ),
            SelectProperty(
                id='id',
                type='select',
                name='Status',
                select=SelectOption(
                    id='id',
                    name='Not started',
                    color='red',
                )
            ),
            DateProperty(
                id='id',
                name='Due date',
                type='date',
                date=Date(
                    start=date(2021, 12, 15),
                    end=None
                )
            ),
            TitleProperty(
                id='title',  # It's always title in API repsonse
                name='Name',  # It's always Name in API response
                type='title',
                title=[
                    TextBlock(
                        type='text',
                        annotations=Annotation(),
                        plain_text="This is a test for integration library for Notion API",
                        href=None,
                        text=TextBlockContent(
                            content="This is a test for integration library for Notion API",
                            link=None
                        )
                    )
                ]
            )
        ],
        url='https://www.notion.so/test-page-name-id'
    )

    built_page = PageBuilder.build(raw_data)
    assert built_page == expected_page
