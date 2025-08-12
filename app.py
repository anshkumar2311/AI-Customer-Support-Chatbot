import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Customer Chatbot", layout="wide")

# Beautiful header with background and improved styling
page_bg_img = """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Full page background image */
    .stApp {
    position: relative;
    background-image:
        linear-gradient(rgba(15, 15, 30, 0.8), rgba(15, 15, 30, 0.8)), /* dark overlay */
        url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1350&q=80');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    min-height: 100vh;
    font-family: 'Poppins', sans-serif;
    color: white;
    }

    /* AI-themed subtle pattern overlay */
    .stApp::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url('https://cdn-icons-png.flaticon.com/512/1017/1017441.png'); /* example AI circuit icon */
    background-repeat: repeat;
    background-size: 50px 50px;
    opacity: 0.05;
    pointer-events: none;
    z-index: 0;
    }

    /* Beautiful header overlay */
    .header-overlay {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 25vh;
        text-align: center;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.8) 0%, rgba(118, 75, 162, 0.8) 100%);
        padding: 0.5rem;
        border-radius: 25px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }

    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #ffffff, #f0f0f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 400;
        max-width: 800px;
        line-height: 1.6;
        margin-bottom: 0.5rem;
        opacity: 0.95;
    }

    .hero-badges {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 0.5rem;
    }

    .badge {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }

    .badge:hover {
        background: rgba(255, 255, 255, 0.3);
        transform: translateY(-2px);
    }

    /* Features container */
    .features-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem;
        color: #333;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    .features-title {
        font-size: 2rem;
        font-weight: 600;
        color: #667eea;
        margin-bottom: 2rem;
        text-align: center;
    }

    /* Feature item */
    .feature-item {
        margin-bottom: 0.5rem;
        padding: 1.0rem;
        background: white;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease;
    }

    .feature-item:hover {
        transform: translateX(5px);
    }

    .feature-title {
        font-weight: 600;
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        color: #667eea;
    }

    .feature-desc {
        color: #666;
        line-height: 1.6;
        font-size: 1rem;
    }
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Beautiful header section
st.markdown(
    """
<div class="header-overlay">
    <h1 class="hero-title">🤖 AI Customer Support</h1>
    <p class="hero-subtitle">Experience instant, intelligent customer service powered by advanced AI technology. Get answers to your questions 24/7 with our smart virtual assistant.</p>
    <div class="hero-badges">
        <span class="badge">⚡ Instant Responses</span>
        <span class="badge">🌍 24/7 Available</span>
        <span class="badge">🧠 Smart AI</span>
        <span class="badge">🔒 Secure</span>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Create 2 columns layout
col1, col2 = st.columns([1, 1])

# Left column - Features
with col1:
    st.markdown(
        """
    <div class="features-container">
        <h2 class="features-title">✨ Key Features</h2>
        <div class="feature-item">
            <div class="feature-title">⚡ Instant Responses</div>
            <div class="feature-desc">Our AI chatbot replies to your queries in real-time with no wait</div>
        </div>
        <div class="feature-item">
            <div class="feature-title">🧠 Smart & Contextual</div>
            <div class="feature-desc">Understands your needs and provides accurate, relevant help tailored to your specific situation.</div>
        </div>
        <div class="feature-item">
            <div class="feature-title">🌍 24/7 Availability</div>
            <div class="feature-desc">Always ready to assist, no matter the time zone or hour. Our AI never sleeps.</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Right column - Chatbot
with col2:

    # Embed chatbot in the right column
    chatbot_html = """
    <script type="text/javascript">
      (function(d, t) {
          var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
          v.onload = function() {
            window.voiceflow.chat.load({
              verify: { projectID: '688b52a2c4336541b33113dc' },
              url: 'https://general-runtime.voiceflow.com',
              versionID: 'production',
              voice: {
                url: "https://runtime-api.voiceflow.com"
              }
            });
          };
          v.src = "https://cdn.voiceflow.com/widget-next/bundle.mjs";
          v.type = "text/javascript";
          s.parentNode.insertBefore(v, s);
      })(document, 'script');
    </script>
    """

    components.html(chatbot_html, height=500, width=1000)

# Footer
st.markdown(
    """
<div style="text-align: center; padding: 0.5rem; margin-top: 0.5rem; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border-radius: 15px;">
    <p style="color: white; font-size: 1rem;">
        © 2024 AI Customer Support. Powered by Advanced AI Technology.
    </p>
</div>
""",
    unsafe_allow_html=True,
)
