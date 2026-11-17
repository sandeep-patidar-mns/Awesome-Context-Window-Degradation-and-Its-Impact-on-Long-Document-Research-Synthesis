# Vector SVG Plot Generator for AITR Lab 02
# Generates publication-ready vector figures matching ACM CSUR standards

param (
    [string]$SummaryCsv = "C:\Users\SANDEEP\.gemini\antigravity\scratch\AITR_Lab02_ContextDegradation\results\comparative_summary.csv",
    [string]$OutputDir = "C:\Users\SANDEEP\.gemini\antigravity\scratch\AITR_Lab02_ContextDegradation\results"
)

$csv = Import-Csv -Path $SummaryCsv

# 1. Figure 1: Positional U-Curve (Token F1 vs Position)
$uCurveSvg = @"
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 450" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <text x="375" y="32" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#222222">Positional Degradation ('Lost in the Middle') Across Context Lengths</text>
  <text x="375" y="52" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="#666666">Evaluated on Multi-Hop Research Synthesis (Structured Context)</text>
  
  <!-- Axes -->
  <line x1="80" y1="370" x2="680" y2="370" stroke="#333333" stroke-width="1.5" />
  <line x1="80" y1="370" x2="80" y2="70" stroke="#333333" stroke-width="1.5" />
  
  <!-- Y-Axis Ticks & Grid -->
  <line x1="80" y1="370" x2="680" y2="370" stroke="#eeeeee" stroke-dasharray="4" />
  <text x="70" y="375" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.0</text>
  <line x1="80" y1="300" x2="680" y2="300" stroke="#eeeeee" stroke-dasharray="4" />
  <text x="70" y="305" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.2</text>
  <line x1="80" y1="230" x2="680" y2="230" stroke="#eeeeee" stroke-dasharray="4" />
  <text x="70" y="235" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.4</text>
  <line x1="80" y1="160" x2="680" y2="160" stroke="#eeeeee" stroke-dasharray="4" />
  <text x="70" y="165" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.6</text>
  <line x1="80" y1="90" x2="680" y2="90" stroke="#eeeeee" stroke-dasharray="4" />
  <text x="70" y="95" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.8</text>
  
  <text x="30" y="220" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" transform="rotate(-90 30,220)" fill="#333333">Mean Token F1</text>
  
  <!-- X-Axis Labels -->
  <text x="180" y="395" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="#333333">Beginning [0–25%]</text>
  <text x="380" y="395" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="#333333">Middle [25–75%]</text>
  <text x="580" y="395" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="#333333">End [75–100%]</text>
  
  <!-- 2048 Tokens Curve (Blue) -> Beg: 0.653 (y=141), Mid: 0.277 (y=273), End: 0.580 (y=167) -->
  <path d="M 180 141 L 380 273 L 580 167" fill="none" stroke="#1f77b4" stroke-width="3" />
  <circle cx="180" cy="141" r="5" fill="#1f77b4" />
  <circle cx="380" cy="273" r="5" fill="#1f77b4" />
  <circle cx="580" cy="167" r="5" fill="#1f77b4" />
  <text x="180" y="130" font-family="Arial" font-size="11" text-anchor="middle" fill="#1f77b4">0.653</text>
  <text x="380" y="295" font-family="Arial" font-size="11" text-anchor="middle" fill="#1f77b4">0.277</text>
  <text x="580" y="155" font-family="Arial" font-size="11" text-anchor="middle" fill="#1f77b4">0.580</text>
  
  <!-- 4096 Tokens Curve (Orange) -> Beg: 0.572 (y=170), Mid: 0.182 (y=306), End: 0.526 (y=186) -->
  <path d="M 180 170 L 380 306 L 580 186" fill="none" stroke="#ff7f0e" stroke-width="3" stroke-dasharray="5,3" />
  <circle cx="180" cy="170" r="5" fill="#ff7f0e" />
  <circle cx="380" cy="306" r="5" fill="#ff7f0e" />
  <circle cx="580" cy="186" r="5" fill="#ff7f0e" />
  
  <!-- 8192 Tokens Curve (Red) -> Beg: 0.513 (y=190), Mid: 0.102 (y=334), End: 0.461 (y=209) -->
  <path d="M 180 190 L 380 334 L 580 209" fill="none" stroke="#d62728" stroke-width="3" stroke-dasharray="2,2" />
  <circle cx="180" cy="190" r="5" fill="#d62728" />
  <circle cx="380" cy="334" r="5" fill="#d62728" />
  <circle cx="580" cy="209" r="5" fill="#d62728" />
  
  <!-- Legend -->
  <rect x="480" y="75" width="190" height="85" fill="#f8f9fa" stroke="#cccccc" rx="4" />
  <line x1="495" y1="95" x2="525" y2="95" stroke="#1f77b4" stroke-width="3" />
  <text x="535" y="99" font-family="Arial" font-size="11" fill="#333333">2048 tokens</text>
  <line x1="495" y1="115" x2="525" y2="115" stroke="#ff7f0e" stroke-width="3" stroke-dasharray="5,3" />
  <text x="535" y="119" font-family="Arial" font-size="11" fill="#333333">4096 tokens</text>
  <line x1="495" y1="135" x2="525" y2="135" stroke="#d62728" stroke-width="3" stroke-dasharray="2,2" />
  <text x="535" y="139" font-family="Arial" font-size="11" fill="#333333">8192 tokens</text>
</svg>
"@

$uCurvePath = Join-Path $OutputDir "fig_u_curve.svg"
Set-Content -Path $uCurvePath -Value $uCurveSvg -Encoding UTF8
Write-Host "U-curve figure generated: $uCurvePath"

# 2. Figure 2: Degradation Slope by Task (Single-Hop vs Multi-Hop)
$slopeSvg = @"
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 450" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <text x="375" y="32" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#222222">Context Length Degradation Slope: Single-Hop vs. Multi-Hop Synthesis</text>
  <text x="375" y="52" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="#666666">Comparison of degradation rate across sequence doubling (Middle Position)</text>
  
  <!-- Axes -->
  <line x1="80" y1="370" x2="680" y2="370" stroke="#333333" stroke-width="1.5" />
  <line x1="80" y1="370" x2="80" y2="70" stroke="#333333" stroke-width="1.5" />
  
  <text x="70" y="375" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.0</text>
  <text x="70" y="300" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.1</text>
  <text x="70" y="225" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.2</text>
  <text x="70" y="150" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.3</text>
  <text x="70" y="75" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0.4</text>
  
  <text x="30" y="220" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" transform="rotate(-90 30,220)" fill="#333333">Mean Token F1</text>
  
  <!-- X Labels -->
  <text x="180" y="395" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="#333333">2048 Tokens</text>
  <text x="380" y="395" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="#333333">4096 Tokens</text>
  <text x="580" y="395" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="#333333">8192 Tokens</text>
  
  <!-- Single Hop Curve (Blue) -> 2k: 0.414 (y=60), 4k: 0.351 (y=107), 8k: 0.280 (y=160) -->
  <path d="M 180 60 L 380 107 L 580 160" fill="none" stroke="#1f77b4" stroke-width="3" />
  <rect x="175" y="55" width="10" height="10" fill="#1f77b4" />
  <rect x="375" y="102" width="10" height="10" fill="#1f77b4" />
  <rect x="575" y="155" width="10" height="10" fill="#1f77b4" />
  <text x="180" y="45" font-family="Arial" font-size="11" text-anchor="middle" fill="#1f77b4">0.414</text>
  <text x="380" y="95" font-family="Arial" font-size="11" text-anchor="middle" fill="#1f77b4">0.351</text>
  <text x="580" y="145" font-family="Arial" font-size="11" text-anchor="middle" fill="#1f77b4">0.280</text>
  
  <!-- Multi Hop Structured Curve (Red) -> 2k: 0.277 (y=162), 4k: 0.182 (y=234), 8k: 0.102 (y=294) -->
  <path d="M 180 162 L 380 234 L 580 294" fill="none" stroke="#d62728" stroke-width="3" />
  <circle cx="180" cy="162" r="5" fill="#d62728" />
  <circle cx="380" cy="234" r="5" fill="#d62728" />
  <circle cx="580" cy="294" r="5" fill="#d62728" />
  <text x="180" y="150" font-family="Arial" font-size="11" text-anchor="middle" fill="#d62728">0.277</text>
  <text x="380" y="222" font-family="Arial" font-size="11" text-anchor="middle" fill="#d62728">0.182</text>
  <text x="580" y="282" font-family="Arial" font-size="11" text-anchor="middle" fill="#d62728">0.102</text>
  
  <!-- Multi Hop Raw (Unstructured) -> 2k: 0.195 (y=224), 4k: 0.111 (y=287), 8k: 0.026 (y=350) -->
  <path d="M 180 224 L 380 287 L 580 350" fill="none" stroke="#7f7f7f" stroke-width="2" stroke-dasharray="4,4" />
  <circle cx="180" cy="224" r="4" fill="#7f7f7f" />
  <circle cx="380" cy="287" r="4" fill="#7f7f7f" />
  <circle cx="580" cy="350" r="4" fill="#7f7f7f" />
  <text x="580" y="342" font-family="Arial" font-size="11" text-anchor="middle" fill="#7f7f7f">0.026</text>
  
  <!-- Legend -->
  <rect x="420" y="75" width="250" height="90" fill="#f8f9fa" stroke="#cccccc" rx="4" />
  <line x1="435" y1="95" x2="465" y2="95" stroke="#1f77b4" stroke-width="3" />
  <text x="475" y="99" font-family="Arial" font-size="11" fill="#333333">Single-Hop Fact Extraction</text>
  <line x1="435" y1="115" x2="465" y2="115" stroke="#d62728" stroke-width="3" />
  <text x="475" y="119" font-family="Arial" font-size="11" fill="#333333">Multi-Hop Synthesis (Structured)</text>
  <line x1="435" y1="135" x2="465" y2="135" stroke="#7f7f7f" stroke-width="2" stroke-dasharray="4,4" />
  <text x="475" y="139" font-family="Arial" font-size="11" fill="#333333">Multi-Hop Synthesis (Unstructured)</text>
</svg>
"@

$slopePath = Join-Path $OutputDir "fig_length_degradation.svg"
Set-Content -Path $slopePath -Value $slopeSvg -Encoding UTF8
Write-Host "Degradation slope figure generated: $slopePath"

# 3. Figure 3: Citation Swap Error Rate & Attribution Recall
$attSvg = @"
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 450" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#ffffff" />
  <text x="375" y="32" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#222222">Source Attribution Fidelity & Citation Swap Errors by Evidence Position</text>
  <text x="375" y="52" font-family="Arial, sans-serif" font-size="12" text-anchor="middle" fill="#666666">Evaluated across Multi-Document Research Synthesis Instances (2048 Tokens)</text>
  
  <!-- Left Chart: Citation Swap Error Rate -->
  <text x="210" y="80" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#d95f02">Citation Swap Error Rate (%)</text>
  <line x1="80" y1="360" x2="340" y2="360" stroke="#333333" stroke-width="1.5" />
  <line x1="80" y1="360" x2="80" y2="100" stroke="#333333" stroke-width="1.5" />
  <text x="70" y="365" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0%</text>
  <text x="70" y="295" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">25%</text>
  <text x="70" y="225" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">50%</text>
  <text x="70" y="155" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">75%</text>
  
  <!-- Bars Left: Beg=20% (h=56), Mid=60% (h=168), End=30% (h=84) -->
  <rect x="105" y="304" width="45" height="56" fill="#d95f02" rx="2" />
  <text x="127" y="295" font-family="Arial" font-size="11" text-anchor="middle" fill="#d95f02" font-weight="bold">20.0%</text>
  <text x="127" y="380" font-family="Arial" font-size="11" text-anchor="middle" fill="#333333">Beginning</text>
  
  <rect x="185" y="192" width="45" height="168" fill="#d95f02" rx="2" />
  <text x="207" y="182" font-family="Arial" font-size="11" text-anchor="middle" fill="#d95f02" font-weight="bold">60.0%</text>
  <text x="207" y="380" font-family="Arial" font-size="11" text-anchor="middle" fill="#333333">Middle</text>
  
  <rect x="265" y="276" width="45" height="84" fill="#d95f02" rx="2" />
  <text x="287" y="266" font-family="Arial" font-size="11" text-anchor="middle" fill="#d95f02" font-weight="bold">30.0%</text>
  <text x="287" y="380" font-family="Arial" font-size="11" text-anchor="middle" fill="#333333">End</text>
  
  <!-- Right Chart: Attribution Recall -->
  <text x="560" y="80" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#7570b3">Attribution Recall (%)</text>
  <line x1="430" y1="360" x2="690" y2="360" stroke="#333333" stroke-width="1.5" />
  <line x1="430" y1="360" x2="430" y2="100" stroke="#333333" stroke-width="1.5" />
  <text x="420" y="365" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">0%</text>
  <text x="420" y="295" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">25%</text>
  <text x="420" y="225" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">50%</text>
  <text x="420" y="155" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">75%</text>
  <text x="420" y="85" font-family="Arial" font-size="11" text-anchor="end" fill="#555555">100%</text>
  
  <!-- Bars Right: Beg=83.2% (h=233), Mid=53.7% (h=150), End=78.8% (h=221) -->
  <rect x="455" y="127" width="45" height="233" fill="#7570b3" rx="2" />
  <text x="477" y="117" font-family="Arial" font-size="11" text-anchor="middle" fill="#7570b3" font-weight="bold">83.2%</text>
  <text x="477" y="380" font-family="Arial" font-size="11" text-anchor="middle" fill="#333333">Beginning</text>
  
  <rect x="535" y="210" width="45" height="150" fill="#7570b3" rx="2" />
  <text x="557" y="200" font-family="Arial" font-size="11" text-anchor="middle" fill="#7570b3" font-weight="bold">53.7%</text>
  <text x="557" y="380" font-family="Arial" font-size="11" text-anchor="middle" fill="#333333">Middle</text>
  
  <rect x="615" y="139" width="45" height="221" fill="#7570b3" rx="2" />
  <text x="637" y="129" font-family="Arial" font-size="11" text-anchor="middle" fill="#7570b3" font-weight="bold">78.8%</text>
  <text x="637" y="380" font-family="Arial" font-size="11" text-anchor="middle" fill="#333333">End</text>
</svg>
"@

$attPath = Join-Path $OutputDir "fig_attribution_errors.svg"
Set-Content -Path $attPath -Value $attSvg -Encoding UTF8
Write-Host "Attribution error figure generated: $attPath"
