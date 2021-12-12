import json
from datetime import datetime, timezone
from autonotion.models.blocks import Annotation, TextBlock, TextBlockContent
from autonotion.models.database import Database
from autonotion.models.builder import DatabaseBuilder
from autonotion.models.pages import WorkspaceParent
from autonotion.models.properties import FormulaExpression, TitleProperty

from autonotion.models.properties import (
    CreatedTime,
    DateProperty,
    FormulaProperty,
    MultiSelectProperty,
    PeopleProperty,
    SelectOption,
    SelectProperty,
    TitleProperty,
    OptionGroup
)

def test_database_builder_create_database_from_api_response(database):
    """
    Test the creation of a database.
    """
    expected = Database(
        object='database',
        id='id',
        cover=None,
        icon=None,
        created_time=datetime(2021, 12, 3, 19, 56, 0, tzinfo=timezone.utc),
        last_edited_time=datetime(2021, 12, 6, 23, 47, 0, tzinfo=timezone.utc),
        title=[
            TextBlock(
                type='text',
                annotations=Annotation(),
                plain_text='API Test Board',
                href=None,
                text=TextBlockContent(
                    content="API Test Board",
                    link=None
                )
            )
        ],
        properties=[
            FormulaProperty(
                type='formula',
                id='id',
                name='Formula 1',
                formula=FormulaExpression(
                    expression='formatDate(prop("Due date"), "DD/MM/YY HH:mm")'
                )
            ),
            MultiSelectProperty(
                id='id',
                type='multi_select',
                name="Labels",
                multi_select=OptionGroup(
                    options=[
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
            ),
            CreatedTime(
                name="Created time",
                id="id",
                type="created_time",
                created_time={}
            ),
            PeopleProperty(
                type='people',
                id='id',
                name='Assign',
                people={}
            ),
            SelectProperty(
                id='id',
                type='select',
                name='Status',
                select=OptionGroup(
                    options=[
                        SelectOption(
                            id='1',
                            name='Not started',
                            color='red'
                        ),
                        SelectOption(
                            id='2',
                            name='In progress',
                            color='yellow'
                        ),
                        SelectOption(
                            id='3',
                            name='Completed',
                            color='green'
                        ),
                    ]
                )
            ),
            DateProperty(
                id='id',
                name='Due date',
                type='date',
                date={}
            ),
            TitleProperty(
                id='title',  # It's always title in API repsonse
                name='Name',  # It's always Name in API response
                type='title',
                title={}
            )
        ],
        parent=WorkspaceParent(
            type='workspace',
            workspace=True
        ),
        url="https://www.notion.so/database_id"
    )

    data = json.loads(database)
    built_database = DatabaseBuilder.build(data)
    assert built_database == expected