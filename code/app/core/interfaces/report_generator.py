from typing import List
from abc import ABC, abstractmethod
from app.core.entities.repository import Repository

class ReportGenerator(ABC):
    """
        Gera um relatório a partir de uma lista de repositórios e salva no caminho de arquivo especificado.

        Parâmetros:
            repos (List[Repository]): Lista de objetos Repository que serão incluídos no relatório.
            file_path (str): Caminho do arquivo onde o relatório será salvo.

        Retorna:
            None
    """
    @abstractmethod
    def generate(self, repos: List[Repository], file_path: str) -> None:
        pass