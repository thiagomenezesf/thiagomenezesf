from pathlib import Path
import re

INPUT = Path("github-calendar-raw.svg")
OUTPUT = Path("github-calendar.svg")

if not INPUT.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {INPUT}")

svg = INPUT.read_text(encoding="utf-8")

# Aumenta a área externa para dar espaço ao novo layout
svg = re.sub(
    r'<svg([^>]*?)width="480"([^>]*?)height="129"([^>]*)>',
    r'<svg\1width="800"\2height="190"\3>',
    svg,
    count=1,
)

# Título
svg = svg.replace(
    "Contributions calendar",
    "Contribution Activity"
)

# Aumenta a área do calendário interno
svg = svg.replace(
    'viewBox="0,0 795,130"',
    'viewBox="0,0 795,155"'
)

# Adiciona elementos visuais antes do fechamento do calendário
marker = "</svg>\n                    </section>"

extra = """
    <!-- Meses -->
    <g class="calendar-months"
       font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
       font-size="13"
       fill="#777">

        <text x="45"  y="12">Jan</text>
        <text x="105" y="12">Fev</text>
        <text x="165" y="12">Mar</text>
        <text x="225" y="12">Abr</text>
        <text x="285" y="12">Mai</text>
        <text x="345" y="12">Jun</text>
        <text x="405" y="12">Jul</text>
        <text x="465" y="12">Ago</text>
        <text x="525" y="12">Set</text>
        <text x="585" y="12">Out</text>
        <text x="645" y="12">Nov</text>
        <text x="705" y="12">Dez</text>
    </g>

    <!-- Legenda -->
    <g transform="translate(570,140)"
       font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
       font-size="11"
       fill="#777">

        <text x="-42" y="10">Menos</text>

        <rect x="0"  y="0" width="11" height="11" rx="2" fill="#ebedf0"/>
        <rect x="15" y="0" width="11" height="11" rx="2" fill="#9be9a8"/>
        <rect x="30" y="0" width="11" height="11" rx="2" fill="#40c463"/>
        <rect x="45" y="0" width="11" height="11" rx="2" fill="#30a14e"/>
        <rect x="60" y="0" width="11" height="11" rx="2" fill="#216e39"/>

        <text x="78" y="10">Mais</text>
    </g>
"""

if marker in svg:
    svg = svg.replace(
        marker,
        extra + "\n" + marker,
        1
    )
else:
    print("Aviso: ponto de inserção do calendário não encontrado.")

OUTPUT.write_text(svg, encoding="utf-8")

print(f"Calendário personalizado criado: {OUTPUT}")
