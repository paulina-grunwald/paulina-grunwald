import sys

def create_animated_header(filename):
    svg_content = '''<svg width="800" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f0c29;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#302b63;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#24243e;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00ffff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ff00ff;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      .typing-text {
        font-family: 'Courier New', Courier, monospace;
        font-size: 50px;
        font-weight: bold;
        fill: url(#text-grad);
        filter: url(#glow);
      }
      .cursor {
        font-size: 50px;
        fill: #00ffff;
        animation: blink 1s infinite;
      }
      @keyframes blink {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
      }
      .sub-text {
        font-family: sans-serif;
        font-size: 20px;
        fill: #a0a0a0;
        opacity: 0;
        animation: fadeIn 2s forwards;
        animation-delay: 3s;
      }
      @keyframes fadeIn {
        to { opacity: 1; }
      }
    </style>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg-grad)" rx="15" ry="15" />

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

  <!-- Decorative Elements -->
  <circle cx="750" cy="40" r="20" fill="none" stroke="#00ffff" stroke-width="2" opacity="0.5" />
  <circle cx="750" cy="40" r="10" fill="#ff00ff" opacity="0.5">
    <animate attributeName="r" values="10;15;10" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>'''

    with open(filename, 'w') as f:
        f.write(svg_content)
    print(f"Created {filename}")

if __name__ == "__main__":
    create_animated_header("assets/header_animated.svg")
