import sys
import random

def create_space_motion_header(filename):
    # Generate random stars
    stars = ""
    for _ in range(50):
        cx = random.randint(0, 800)
        cy = random.randint(0, 200)
        r = random.uniform(0.5, 2.0)
        opacity = random.uniform(0.3, 1.0)
        duration = random.uniform(2, 5)
        stars += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" opacity="{opacity}"><animate attributeName="opacity" values="{opacity};0.1;{opacity}" dur="{duration}s" repeatCount="indefinite" /></circle>'

    svg_content = f'''<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="space-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f0c29;stop-opacity:1">
        <animate attributeName="stop-color" values="#0f0c29;#24243e;#0f0c29" dur="10s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" style="stop-color:#302b63;stop-opacity:1">
        <animate attributeName="stop-color" values="#302b63;#0f0c29;#302b63" dur="10s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" style="stop-color:#24243e;stop-opacity:1">
        <animate attributeName="stop-color" values="#24243e;#302b63;#24243e" dur="10s" repeatCount="indefinite" />
      </stop>
    </linearGradient>

    <filter id="glow">
      <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <style>
      .typing-text {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 50px;
        font-weight: bold;
        fill: #ffffff;
        filter: url(#glow);
      }}
      .cursor {{
        font-size: 50px;
        fill: #00ffff;
        animation: blink 1s infinite;
      }}
      @keyframes blink {{
        0% {{ opacity: 0; }}
        50% {{ opacity: 1; }}
        100% {{ opacity: 0; }}
      }}
      .sub-text {{
        font-family: sans-serif;
        font-size: 20px;
        fill: #a0a0a0;
        opacity: 0;
        animation: fadeIn 2s forwards;
        animation-delay: 3s;
      }}
      @keyframes fadeIn {{
        to {{ opacity: 1; }}
      }}
      .planet {{
        fill: url(#planet-grad);
        filter: url(#glow);
        animation: float 10s ease-in-out infinite;
      }}
      @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
        100% {{ transform: translateY(0px); }}
      }}
    </style>
    <radialGradient id="planet-grad" cx="50%" cy="50%" r="50%" fx="50%" fy="50%">
      <stop offset="0%" style="stop-color:#ff00ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#302b63;stop-opacity:0" />
    </radialGradient>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#space-grad)" rx="15" ry="15" />

  <!-- Stars -->
  {stars}

  <!-- Planet/Orb -->
  <circle cx="700" cy="100" r="60" class="planet" opacity="0.6" />

  <!-- Animated Text -->
  <text x="50" y="100" class="typing-text">
    Hi there, I'm Paulina!
  </text>

  <!-- Blinking Cursor -->
  <text x="700" y="100" class="cursor">_</text>

  <!-- Subtitle -->
  <text x="50" y="150" class="sub-text">
    Senior Software Engineer | Agentic AI Enthusiast
  </text>
</svg>'''

    with open(filename, 'w') as f:
        f.write(svg_content)
    print(f"Created {filename}")

if __name__ == "__main__":
    create_space_motion_header("assets/header_animated.svg")
