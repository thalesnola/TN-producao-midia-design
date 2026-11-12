# Script deterministico para geracao de docs/diagrama-motion.svg
# Compativel 100% com sanitizador do GitHub (SVG Puro sem <filter> e sem style= inline)

import pathlib

SVG_CONTENT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 920" width="1000" height="920">
  <defs>
    <!-- Degradê de fundo suave Motion -->
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F3EEFF"/>
      <stop offset="50%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E9F7FF"/>
    </linearGradient>

    <!-- Ambient Glows em SVG Puro (substitui feGaussianBlur compatível com GitHub) -->
    <radialGradient id="glow_pink" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF7AC6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FF7AC6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_blue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2F9BFF" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#2F9BFF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_purple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_green" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
    </radialGradient>

    <!-- Motion Trails Diagonais -->
    <linearGradient id="trail_purple" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8A5CF6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#8A5CF6" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#8A5CF6" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="trail_blue" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Fundo -->
  <rect width="1000" height="920" fill="url(#bg)"/>

  <!-- Ambient Glows -->
  <circle cx="910" cy="110" r="230" fill="url(#glow_pink)"/>
  <circle cx="90" cy="790" r="250" fill="url(#glow_blue)"/>
  <circle cx="500" cy="330" r="280" fill="url(#glow_purple)"/>

  <!-- Motion Trails Diagonais (-12deg) -->
  <rect x="120" y="80" width="280" height="26" rx="13" fill="url(#trail_purple)" transform="rotate(-12 260 93)"/>
  <rect x="680" y="440" width="260" height="24" rx="12" fill="url(#trail_blue)" transform="rotate(-12 810 452)"/>
  <rect x="60" y="36" width="354.0" height="26" rx="13" fill="#FCE7F3" stroke="#FBCFE8" stroke-width="1"/>
  <text x="237.0" y="53" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#DB2777" text-anchor="middle" letter-spacing="0.5">MULTIMÍDIA · 3D, VÍDEO &amp; DESIGN PROGRAMÁTICO</text><text x="60" y="86" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="26" font-weight="800" fill="#1B1F3B">TN-producao-midia-design · Hub Criativo por Código</text><text x="60" y="114" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="500" fill="#4A5568">Automação 3D com Blender, vídeos programáticos em Remotion e composições web em HyperFrames.</text>
  <rect x="122" y="158" width="760" height="70" rx="16" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="121" y="154" width="760" height="70" rx="16" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="120" y="150" width="760" height="70" rx="16" fill="#1B1F3B" stroke="#334155" stroke-width="1.5"/><rect x="140" y="162" width="130" height="20" rx="10" fill="#EC4899"/><text x="205" y="176" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#FFFFFF" text-anchor="middle">SPEC DO PROJETO</text><text x="285" y="177" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF">Briefing Declarativo em JSON / Markdown</text><text x="140" y="204" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#F472B6">Define paleta de cores, timing de cenas, roteiro sonoro e geometria 3D sem intervenção manual.</text><line x1="500" y1="220" x2="500" y2="255" stroke="#CBD5E1" stroke-width="2"/>
  <rect x="62" y="263" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="61" y="259" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="60" y="255" width="205" height="230" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/><rect x="72" y="267" width="14" height="14" rx="7" fill="#EDE9FE"/><text x="92" y="279" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#7C3AED">Blender 3D</text><text x="72" y="301" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#1B1F3B">Render Fotorrealista</text><text x="72" y="323" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#475569"><tspan x="72" dy="0">• Modelagem procedural</tspan><tspan x="72" dy="17">• Materiais PBR e shaders</tspan><tspan x="72" dy="17">• Exportação GLB/glTF</tspan><tspan x="72" dy="17">• Câmeras cinematográficas</tspan></text>
  <rect x="287" y="263" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="286" y="259" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="285" y="255" width="205" height="230" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/><rect x="297" y="267" width="14" height="14" rx="7" fill="#E0F2FE"/><text x="317" y="279" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#0284C7">Remotion</text><text x="297" y="301" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#1B1F3B">Vídeo em React</text><text x="297" y="323" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#475569"><tspan x="297" dy="0">• Animações em TypeScript</tspan><tspan x="297" dy="17">• Sincronia quadro-a-fala</tspan><tspan x="297" dy="17">• Render em lote MP4 60fps</tspan><tspan x="297" dy="17">• Interatividade modular</tspan></text>
  <rect x="512" y="263" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="511" y="259" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="510" y="255" width="205" height="230" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/><rect x="522" y="267" width="14" height="14" rx="7" fill="#FEF3C7"/><text x="542" y="279" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#D97706">HyperFrames</text><text x="522" y="301" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#1B1F3B">Motion HTML/CSS</text><text x="522" y="323" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#475569"><tspan x="522" dy="0">• Composições na web</tspan><tspan x="522" dy="17">• Timing declarativo data-*</tspan><tspan x="522" dy="17">• Sem dependência pesada</tspan><tspan x="522" dy="17">• Reprodução determinística</tspan></text>
  <rect x="737" y="263" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="736" y="259" width="205" height="230" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="735" y="255" width="205" height="230" rx="14" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5"/><rect x="747" y="267" width="14" height="14" rx="7" fill="#DCFCE7"/><text x="767" y="279" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="700" fill="#16A34A">ArtCraft &amp; SVG</text><text x="747" y="301" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="600" fill="#1B1F3B">Vetor Determinístico</text><text x="747" y="323" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="400" fill="#475569"><tspan x="747" dy="0">• Linguagem Motion visual</tspan><tspan x="747" dy="17">• Ícones e diagramas puros</tspan><tspan x="747" dy="17">• Ambient glows e elevação</tspan><tspan x="747" dy="17">• Zero distorção em 4K</tspan></text>
  <!-- BLOCO DE DEMONSTRAÇÃO PRÁTICA -->
  
  <rect x="62" y="563" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="61" y="559" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="60" y="555" width="880" height="220" rx="22" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  
  <rect x="80" y="569" width="225" height="24" rx="12" fill="#1B1F3B"/>
  <text x="192" y="585" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="800" fill="#60A5FA" text-anchor="middle" letter-spacing="0.8">DEMONSTRAÇÃO PRÁTICA</text>
  <text x="320" y="586" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="600" fill="#64748B">Fluxo operacional concreto do repositório</text>
  
  <!-- Coluna 1: Entrada -->
  
  <rect x="84" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="83" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="82" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.5"/>
  <rect x="94" y="617" width="90" height="20" rx="10" fill="#EDE9FE"/>
  <text x="139" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#7C3AED" text-anchor="middle">SPEC DE ANIMAÇÃO</text>
  <text x="96" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">spec.json Declarativo</text>
  <text x="96" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="96" dy="0">Arquivo descreve roteiro,</tspan><tspan x="96" dy="16">estilo visual e elementos 3D</tspan><tspan x="96" dy="16">com coordenadas e durações.</tspan></text>
  
  <!-- Seta 1 -> 2 -->
  <circle cx="359" cy="682.5" r="14" fill="#EDE9FE" stroke="#C4B5FD" stroke-width="1.5"/>
  <text x="359" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#7C3AED" text-anchor="middle">→</text>
  
  <!-- Coluna 2: Processamento -->
  
  <rect x="379" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="378" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="377" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.5"/>
  <rect x="389" y="617" width="125" height="20" rx="10" fill="#E0F2FE"/>
  <text x="451" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#0284C7" text-anchor="middle">RENDER AUTOMATIZADO</text>
  <text x="391" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Orquestração por Scripts</text>
  <text x="391" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="391" dy="0">Python aciona Blender headless,</tspan><tspan x="391" dy="16">Remotion compila transições e</tspan><tspan x="391" dy="16">assets vetoriais são injetados.</tspan></text>
  
  <!-- Seta 2 -> 3 -->
  <circle cx="654" cy="682.5" r="14" fill="#E0F2FE" stroke="#7DD3FC" stroke-width="1.5"/>
  <text x="654" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#0284C7" text-anchor="middle">→</text>
  
  <!-- Coluna 3: Saída -->
  
  <rect x="674" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="673" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="672" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="684" y="617" width="105" height="20" rx="10" fill="#DCFCE7"/>
  <text x="736" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#16A34A" text-anchor="middle">VÍDEO CONCLUÍDO</text>
  <text x="686" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">MP4 60fps Pronto</text>
  <text x="686" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="686" dy="0">Produto audiovisual de alta</tspan><tspan x="686" dy="16">qualidade entregue sem abrir</tspan><tspan x="686" dy="16">nenhum software gráfico manual.</tspan></text>
  <!-- Faixa Navy Inferior de Conclusão Técnica -->
  <rect x="60" y="800" width="880" height="64" rx="18" fill="#1B1F3B"/>
  <circle cx="95" cy="832" r="15" fill="#3B82F6" fill-opacity="0.25"/>
  <text x="95" y="837" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="15" font-weight="800" fill="#60A5FA" text-anchor="middle">✓</text>
  <text x="125" y="829" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Criação Visual Escalável por Código</text>
  <text x="125" y="848" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#94A3B8">Pipelines reprodutíveis que convertem especificações lógicas em experiências visuais sofisticadas.</text>
</svg>'''

def main():
    p = pathlib.Path(__file__).parent.parent / 'docs' / 'diagrama-motion.svg'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(SVG_CONTENT, encoding='utf-8')
    print('SVG gerado em:', p)

if __name__ == '__main__':
    main()
