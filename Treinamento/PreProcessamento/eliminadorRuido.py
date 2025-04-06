import re
from .anonimazer import anomalizer


def tornar_texto_legivel_humano(texto):
    cleaning_patterns = [
            # Links e imagens do estilo |!url!|
        (r'\|!https?://[^|]+!\|', ' '),

        # URLs simples
        (r'https?://\S+', ' '),

        # Remover artefatos tipo {color:white}...{color}
        (r'\{color[^}]*\}', ' '),

        # Anexos tipo [arquivo.ext|url]
        (r'\[[^\[\]]+\.(pdf|jpe?g|png|docx?|xlsx?)\|[^\]]+\]', ' ', re.IGNORECASE),

        # Tags tipo <[...]> ou com #gccode#
        (r'<\[[^\]]+\]>', ' '),
        (r'#gccode#[^#]+#', ' '),

        # Cabeçalhos tipo h4. Nome
        (r'\|?h\d+\.\s*[\w ]+', ' '),

        # Linhas com "*N anexos*"
        (r'\*\s*\d+\s*anexos?\s*\*', ' '),

        # Limpeza de colunas tipo | |
        (r'\|\s*\|', ' '),
        (r'\|+', ' '),

        # Restos de colchetes e chaves
        (r'[\[\]\{\}]', ' '),

        # Remover múltiplas quebras de linha
        (r'[\r\n]+', ' '),

        # Artefatos como "! <", "! < !", barra invertida etc
        (r'!\s*<\s*!?', ' '),
        (r'\\', ' '),

        # Espaços duplicados
        (r'\s{2,}', ' ')
    
        ]
    
    for pattern in cleaning_patterns:
        if len(pattern) == 3:
            texto = re.sub(pattern[0], pattern[1], texto, flags=pattern[2])
        else:
            texto = re.sub(pattern[0], pattern[1], texto)
    
    texto = anomalizer(texto)

    return texto.strip()
