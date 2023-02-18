from typing import TYPE_CHECKING, Dict

from slither.core.variables.top_level_variable import TopLevelVariable
from slither.solc_parsing.declarations.caller_context import CallerContextExpression
from slither.solc_parsing.variables.variable_declaration import VariableDeclarationSolc

if TYPE_CHECKING:
    from slither.core.compilation_unit import SlitherCompilationUnit
    from slither.solc_parsing.slither_compilation_unit_solc import (
        SlitherCompilationUnitSolc,
    )


class TopLevelVariableSolc(VariableDeclarationSolc, CallerContextExpression):
    def __init__(
        self,
        variable: TopLevelVariable,
        variable_data: Dict,
        slither_parser: "SlitherCompilationUnitSolc",
    ) -> None:
        super().__init__(variable, variable_data)
        self._slither_parser = slither_parser

    @property
    def is_compact_ast(self) -> bool:
        return self._slither_parser.is_compact_ast

    @property
    def compilation_unit(self) -> "SlitherCompilationUnit":
        return self._slither_parser.compilation_unit

    def get_key(self) -> str:
        return self._slither_parser.get_key()

    @property
    def slither_parser(self) -> "SlitherCompilationUnitSolc":
        return self._slither_parser

    @property
    def underlying_variable(self) -> TopLevelVariable:
        # Todo: Not sure how to overcome this with mypy
        assert isinstance(self._variable, TopLevelVariable)
        return self._variable
