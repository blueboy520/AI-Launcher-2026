import streamlit as st
import webbrowser

# --- 页面配置 ---
st.set_page_config(
    page_title="2026 AI工具箱",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 自定义样式 (优化手机端显示) ---
st.markdown("""
<style>
    .stButton button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    .tool-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #e0e0e0;
    }
    /* 调整标题间距 */
    h3 { padding-top: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 数据源 (基于你的思维导图) ---
# link 为空字符串时，系统会自动生成 Google 搜索链接
tools_data = [
    {"category": "🌌 AI大模型", "name": "Gemini 3 Pro", "desc": "谷歌六边形战士，多模态/代码/查数据", "link": "https://gemini.google.com/"},
    {"category": "🌌 AI大模型", "name": "豆包 (Doubao)", "desc": "国内平替，覆盖90%场景", "link": "https://www.doubao.com/"},
    {"category": "🌌 AI大模型", "name": "DeepSeek", "desc": "开源强模型，生态稍弱", "link": "https://chat.deepseek.com/"},
    
    {"category": "🎨 AI绘画", "name": "Banana Pro", "desc": "谷歌出品，生图/改图/海报 (需翻墙)", "link": ""},
    {"category": "🎨 AI绘画", "name": "即梦 (Jimeng)", "desc": "国内平替，质量极高", "link": "https://jimeng.jianying.com/"},
    
    {"category": "🎬 AI视频", "name": "Sora / Veo 3.1", "desc": "音画同步表现突出", "link": ""},
    {"category": "🎬 AI视频", "name": "Wan 2.6", "desc": "AI演员，角色一致性好", "link": ""},
    {"category": "🎬 AI视频", "name": "Runway", "desc": "视频像P图一样编辑", "link": "https://runwayml.com/"},
    {"category": "🎬 AI视频", "name": "Seedance 1.5", "desc": "支持方言口型同步", "link": ""},

    {"category": "🎵 AI音频", "name": "Suno", "desc": "音乐生成，目前无对手", "link": "https://suno.com/"},
    {"category": "🎵 AI音频", "name": "ElevenLabs", "desc": "70+语言音色克隆", "link": "https://elevenlabs.io/"},
    {"category": "🎵 AI音频", "name": "MiniMax", "desc": "中文语音克隆表现好", "link": "https://api.minimax.chat/"},

    {"category": "💻 AI编程", "name": "Antigravity", "desc": "谷歌IDE，内置Gemini 3 Pro", "link": "https://idx.google.com/"}, # 目前叫IDX
    {"category": "💻 AI编程", "name": "Claude Code", "desc": "代码能力强，国内难访问", "link": "https://claude.ai/"},

    {"category": "📚 办公学习", "name": "NotebookLM", "desc": "资料整理/生成播客/导图", "link": "https://notebooklm.google/"},
    {"category": "📚 办公学习", "name": "Banana Pro PPT", "desc": "生成PPT导出PDF+WPS编辑", "link": ""},
    
    {"category": "🤖 数字人/流", "name": "HeyGen", "desc": "口型最准的数字人 (贵)", "link": "https://www.heygen.com/"},
    {"category": "🤖 数字人/流", "name": "n8n", "desc": "节点式工作流，可本地部署", "link": "https://n8n.io/"},
    {"category": "🤖 数字人/流", "name": "飞书多维表格", "desc": "搭建AI自动化业务流", "link": "https://www.feishu.cn/product/base"},
]

# --- 侧边栏 ---
st.sidebar.title("🧰 工具导航")
categories = sorted(list(set([item["category"] for item in tools_data])))
selected_cats = st.sidebar.multiselect("筛选分类", categories, default=categories)
search_term = st.sidebar.text_input("🔍 搜索工具", "")

st.title("🚀 2026 AI 军火库")
st.caption("基于思维导图整理 · 你的个人生产力中台")
st.divider()

# --- 主体展示逻辑 ---
filtered_tools = [
    t for t in tools_data 
    if t["category"] in selected_cats 
    and (search_term.lower() in t["name"].lower() or search_term.lower() in t["desc"].lower())
]

# 按分类分组显示
for cat in categories:
    # 检查该分类下是否有被筛选出的工具
    cat_tools = [t for t in filtered_tools if t["category"] == cat]
    
    if cat_tools:
        st.subheader(cat)
        cols = st.columns(3) # 电脑端3列，手机端会自动堆叠
        for idx, tool in enumerate(cat_tools):
            with cols[idx % 3]:
                with st.container(border=True):
                    st.markdown(f"#### **{tool['name']}**")
                    st.caption(tool['desc'])
                    
                    # 链接处理：如果有链接直接跳转，没有则搜索
                    target_url = tool['link'] if tool['link'] else f"https://www.google.com/search?q={tool['name']}+AI+tool"
                    btn_label = "🚀 启动" if tool['link'] else "🔍 搜索"
                    
                    st.link_button(btn_label, target_url, use_container_width=True)

if not filtered_tools:
    st.warning("没有找到匹配的工具，请尝试其他关键词。")

# --- 底部 ---
st.divider()
st.markdown("<div style='text-align: center; color: grey;'>Created by Blueboy520 | 2026 Edition</div>", unsafe_allow_html=True)
