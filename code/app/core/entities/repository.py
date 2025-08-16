from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Repository:
    """
    Representa um repositório do GitHub com várias estatísticas e metadados pertinentes para pesquisa.
    Atributos:
        name (str): O nome do repositório.
        stargazer_count (int): O número de usuários que deram estrela no repositório.
        url (str): A URL do repositório.
        created_at (datetime): A data e hora em que o repositório foi criado.
        updated_at (datetime): A data e hora em que o repositório foi atualizado pela última vez.
        releases_count (int): O número de releases no repositório.
        primary_language (Optional[str]): A linguagem de programação principal usada no repositório.
        merged_pull_requests (int): O número de pull requests que foram mesclados.
        closed_issues (int): O número de issues que foram fechadas.
        total_issues (int): O número total de issues no repositório.
        closed_issues_percentage (float): A porcentagem de issues fechadas em relação ao total de issues.
    Métodos:
        __post_init__():
            Inicializa o atributo closed_issues_percentage depois da criação do objeto.
        __calc_closed_issues_percentage():
            Calcula e define o atributo closed_issues_percentage com base em closed_issues e total_issues.
    """
    name: str
    stargazer_count: int
    url: str
    created_at: datetime
    updated_at: datetime
    releases_count: int
    primary_language: Optional[str]
    merged_pull_requests: int
    closed_issues: int
    total_issues: int
    closed_issues_percentage: float

    def __post_init__(self):
        self.__calc_closed_issues_percentage()

    def __calc_closed_issues_percentage(self) -> None:
        if self.total_issues > 0:
            self.closed_issues_percentage = (self.closed_issues / self.total_issues) * 100
        else:
            self.closed_issues_percentage = 0.0