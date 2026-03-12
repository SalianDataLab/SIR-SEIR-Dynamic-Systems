"""
EPIDEMIX DYNAMIC SYSTEMS - Nano Edition v2.1.
Interface Premium avec focus sur la rigueur scientifique et la lisibilité.
Axes clarifiés, structure optimisée et contenu enrichi.
"""

import numpy as np
import streamlit as st
from scipy.integrate import solve_ivp
import plotly.graph_objects as go

# --- CONFIGURATION PAGE ---
st.set_page_config(
    page_title="Epidemix PRO | Analyse Scientifique",
    page_icon="assets/dashboard_ref.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DESIGN SYSTEM "NANOTECH" (Lisibilité Optimisée) ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
<style>
    /* Base */
    .stApp {
        background: #020617;
        color: #94a3b8;
        font-family: 'Outfit', sans-serif;
    }

    h1, h2, h3, h4 {
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    /* Glass Container */
    .glass-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }

    /* Header Section */
    .nano-header {
        border-left: 5px solid #3b82f6;
        padding-left: 2rem;
        margin-bottom: 3rem;
        background: linear-gradient(90deg, rgba(59,130,246,0.1), transparent);
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .nano-header h1 {
        font-size: 2.5rem;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: -1px;
    }

    /* R0 Dashboard */
    .r0-focus-container {
        text-align: center;
        padding: 3rem;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.05) 0%, transparent 70%);
        border-radius: 20px;
        margin: 1rem 0;
    }
    .r0-value-big {
        font-size: 7rem;
        font-weight: 900;
        color: #fff;
        line-height: 1;
        text-shadow: 0 0 20px rgba(59, 130, 246, 0.3);
    }
    .status-badge {
        display: inline-block;
        padding: 0.4rem 1.2rem;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 1rem;
    }
    .badge-alert { background: #ef4444; color: #fff; }
    .badge-safe { background: #10b981; color: #fff; }

    /* Axis Clarity Label */
    .axis-info {
        font-size: 0.8rem;
        color: #64748b;
        margin-top: 0.5rem;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIQUE SCIENTIFIQUE ---
def sir_model(t, y, beta, gamma, N):
    S, I, R = y
    return [-beta * S * I / N, beta * S * I / N - gamma * I, gamma * I]

def seir_model(t, y, beta, sigma, gamma, N):
    S, E, I, R = y
    return [-beta * S * I / N, beta * S * I / N - sigma * E, sigma * E - gamma * I, gamma * I]

# --- SIDEBAR (SANS EMOJIS) ---
with st.sidebar:
    st.markdown("### CONFIGURATION")
    model_name = st.selectbox("Modèle Dynamique", ["SIR (Standard)", "SEIR (Incubation)", "Étude Comparative"])
    st.markdown("---")
    
    # Paramètres avec descriptions claires
    n_pop = st.number_input("Population Totale (N)", value=1000, help="Somme totale des individus (S+E+I+R)")
    i_start = st.number_input("Infectés Initiaux (I₀)", value=1, help="Nombre de personnes infectées au jour 0")
    
    st.markdown("### Paramètres Epidémiques")
    beta = st.slider("Taux de Transmission (β)", 0.0, 1.0, 0.35, 0.01, help="Probabilité de transmission lors d'un contact")
    gamma = st.slider("Taux de Guérison (γ)", 0.01, 0.5, 0.1, 0.01, help="Inverse de la durée moyenne d'infection (1/D)")
    
    sigma = 0.2
    if "SEIR" in model_name or "Étude" in model_name:
        sigma = st.slider("Taux d'Incubation (σ)", 0.01, 1.0, 0.2, 0.01, help="Vitesse à laquelle les exposés deviennent infectieux")
    
    t_limit = st.slider("Horizon Temporel (Jours)", 30, 365, 120)

# --- CALCULS ---
t_eval = np.linspace(0, t_limit, 1000)
S0 = n_pop - i_start
y0_sir = [S0, i_start, 0]
y0_seir = [S0, 0, i_start, 0]

sol_sir = solve_ivp(sir_model, (0, t_limit), y0_sir, args=(beta, gamma, n_pop), t_eval=t_eval)
sol_seir = solve_ivp(seir_model, (0, t_limit), y0_seir, args=(beta, sigma, gamma, n_pop), t_eval=t_eval)

r0_val = beta / gamma

# --- CONTENU ---

# Header
st.markdown("""
<div class="nano-header">
    <h1>Analyse des Systèmes Dynamiques</h1>
    <div style="font-size: 0.9rem; color: #64748b; font-weight: 500; text-transform: uppercase; letter-spacing: 1px;">
        Étape 1 : Simulation des trajectoires épidémiques SIR & SEIR
    </div>
</div>
""", unsafe_allow_html=True)

# Dashboard R0 (Le point central scientifique)
c1, c2, c3 = st.columns([1, 1.5, 1])
with c2:
    badge_type = "badge-alert" if r0_val >= 1 else "badge-safe"
    badge_txt = "Seuil Épidémique Franchi" if r0_val >= 1 else "Extinction Naturelle"
    st.markdown(f"""
    <div class="r0-focus-container">
        <div style="color: #94a3b8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 3px; font-weight: 700;">Nombre de Reproduction de Base</div>
        <div class="r0-value-big">{r0_val:.2f}</div>
        <div class="status-badge {badge_type}">{badge_txt}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Visualisation & Analyse
def render_scientific_dashboard(data, title, is_seir=False):
    st.subheader(title)
    
    # Structure d'information
    st.markdown("""
    <div style="background: rgba(59, 130, 246, 0.05); border-left: 3px solid #3b82f6; padding: 1rem; margin-bottom: 2rem; font-size: 0.9rem;">
        <b>Interprétation des axes :</b> L'axe horizontal représente le <b>temps écoulé (en jours)</b>. 
        L'axe vertical représente l'<b>effectif de la population</b> par catégorie (Individus).
    </div>
    """, unsafe_allow_html=True)

    # Section Pédagogique : Définition des Compartiments
    with st.expander("Détails des Catégories de Population", expanded=False):
        c_desc1, c_desc2 = st.columns(2)
        with c_desc1:
            st.markdown("""
            **S (Sains / Susceptibles) :** Individus n'ayant pas encore contracté le virus mais capables d'être infectés. Leur nombre diminue à mesure que l'épidémie progresse.
            
            **E (Exposés) :** *Uniquement en SEIR*. Personnes ayant été en contact avec le virus, en phase d'incubation, mais pas encore contagieuses.
            """)
        with c_desc2:
            st.markdown("""
            **I (Infectés / Infectieux) :** Individus porteurs du virus et capables de le transmettre à la catégorie S. C'est la variable critique pour le système de santé.
            
            **R (Rétablis / Retirés) :** Individus ayant surmonté l'infection (ou isolés). Ils sont considérés comme immunisés et ne participent plus à la chaîne de transmission.
            """)

    # Métriques Clés Stylisées
    cols = st.columns(3)
    idx_target = 2 if is_seir else 1
    peak_y = np.max(data.y[idx_target])
    peak_x = t_eval[np.argmax(data.y[idx_target])]
    
    with cols[0]:
        st.markdown(f"""
        <div class="glass-card">
            <div style="font-size: 0.7rem; font-weight: 800; color: #64748b; text-transform: uppercase;">Intensité Max du Pic</div>
            <div style="font-size: 1.8rem; font-weight: 900; color: #fff;">{int(peak_y)}</div>
            <div style="font-size: 0.75rem;">Infectés simultanés</div>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"""
        <div class="glass-card">
            <div style="font-size: 0.7rem; font-weight: 800; color: #64748b; text-transform: uppercase;">Date Critique</div>
            <div style="font-size: 1.8rem; font-weight: 900; color: #fff;">Jour {int(peak_x)}</div>
            <div style="font-size: 0.75rem;">Moment de charge max.</div>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        recovered_final = (data.y[-1][-1]/n_pop)*100
        st.markdown(f"""
        <div class="glass-card">
            <div style="font-size: 0.7rem; font-weight: 800; color: #64748b; text-transform: uppercase;">Bilan Final</div>
            <div style="font-size: 1.8rem; font-weight: 900; color: #fff;">{recovered_final:.1f}%</div>
            <div style="font-size: 0.75rem;">Taux d'attaque total</div>
        </div>
        """, unsafe_allow_html=True)

    # Graphique Plotly (LISIBILITÉ MAXIMALE)
    fig = go.Figure()
    colors = ['#3b82f6', '#f59e0b', '#ef4444', '#10b981']
    names = ['Sains (S)', 'Exposés (E)', 'Infectés (I)', 'Rétablis (R)']
    
    if is_seir:
        for i in range(4):
            fig.add_trace(go.Scatter(x=t_eval, y=data.y[i], name=names[i], 
                                     line=dict(color=colors[i], width=3 if i==2 else 2)))
    else:
        for i, idx in enumerate([0, 1, 2]):
            actual_name = names[0] if i==0 else (names[2] if i==1 else names[3])
            actual_color = colors[0] if i==0 else (colors[2] if i==1 else colors[3])
            fig.add_trace(go.Scatter(x=t_eval, y=data.y[idx], name=actual_name, 
                                     line=dict(color=actual_color, width=3 if i==1 else 2)))

    # Configuration des axes (DÉCRITS EXPLICITEMENT)
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8', size=12),
        hovermode="x unified",
        margin=dict(l=50, r=20, t=20, b=50),
        xaxis=dict(
            title="TEMPS (JOURS)", 
            showgrid=True, gridcolor='rgba(255,255,255,0.05)',
            linewidth=1, linecolor='rgba(255,255,255,0.2)',
            title_font=dict(size=14, color='#fff')
        ),
        yaxis=dict(
            title="POPULATION (INDIVIDUS)", 
            showgrid=True, gridcolor='rgba(255,255,255,0.05)',
            linewidth=1, linecolor='rgba(255,255,255,0.2)',
            title_font=dict(size=14, color='#fff')
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)

if "SIR" in model_name:
    render_scientific_dashboard(sol_sir, "Évolution du Modèle SIR")
elif "SEIR" in model_name:
    render_scientific_dashboard(sol_seir, "Évolution du Modèle SEIR (avec temps d'incubation)", is_seir=True)
else:
    st.subheader("Étude Comparative : Impact de la phase de latence")
    fig_comp = go.Figure()
    fig_comp.add_trace(go.Scatter(x=t_eval, y=sol_sir.y[1], name="Flux Infectieux SIR (Direct)", line=dict(color='#ef4444', width=3)))
    fig_comp.add_trace(go.Scatter(x=t_eval, y=sol_seir.y[2], name="Flux Infectieux SEIR (Latent)", line=dict(color='#fff', width=3, dash='dash')))
    
    fig_comp.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#94a3b8'),
        xaxis=dict(title="JOURS", gridcolor='rgba(255,255,255,0.05)'),
        yaxis=dict(title="NOMBRE D'INFECTÉS", gridcolor='rgba(255,255,255,0.05)'),
        margin=dict(l=50, r=20, t=10, b=50)
    )
    st.plotly_chart(fig_comp, use_container_width=True)
    st.markdown("""
    <div class="glass-card" style="font-size: 0.85rem;">
        <b>Analyse :</b> On observe que l'introduction du compartiment <i>Exposés</i> (E) décale le pic dans le temps et réduit son amplitude maximale. 
        C'est un comportement typique des systèmes dynamiques où une étape supplémentaire de transition ajoute de l'inertie.
    </div>
    """, unsafe_allow_html=True)

# Footer Scientifique
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #475569; font-size: 0.7rem; padding: 2rem; font-weight: 700; text-transform: uppercase;">
    Projet Mathématiques pour l'IA | Étape 1 : Modélisation des Systèmes Dynamiques | Calcul par intégrateur RK45
</div>
""", unsafe_allow_html=True)
