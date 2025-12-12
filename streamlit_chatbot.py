import pandas as pd
import streamlit as st
import sys


st.set_page_config(
    page_title="Chennai Colleges Chatbot",
    page_icon="🏫",
    layout="wide"
)


st.markdown("""
<style>
    .stChatMessage {
        padding: 12px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 12px;
        border-radius: 10px 10px 0 10px;
    }
    .bot-message {
        background-color: #f5f5f5;
        padding: 12px;
        border-radius: 10px 10px 10px 0;
    }
</style>
""", unsafe_allow_html=True)


st.title("🏫 Chennai Colleges Chatbot")
st.markdown("Ask me about colleges in Chennai! I have information on 35+ colleges.")


with st.sidebar:
    st.header("📊 About")
    st.write("This chatbot helps you find information about colleges in Chennai.")
    st.write("**Features:**")
    st.write("• Search by college name")
    st.write("• Search by location/area")
    st.write("• Get complete college details")
    st.divider()
    st.write("💡 **Try asking:**")
    st.write("- 'Anna University'")
    st.write("- 'Colleges in Guindy'")
    st.write("- 'SRM Institute'")
    st.write("- 'Medical colleges'")


# Load CSV
try:
    df = pd.read_csv("colleges_csvfile.csv", delimiter=',')
    st.sidebar.success(f"✅ Loaded {len(df)} colleges")
except Exception as e:
    st.error(f"CSV file error: {e}")
    df = pd.DataFrame()


# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi Buddy! I can help you find information about colleges in Chennai. How can I assist you today?"}
    ]


# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chatbot response function
def chatbot_response(user_input):
    user = user_input.lower()
    
    # Check if dataframe is loaded
    if df.empty:
        return "Database not loaded. Please check CSV file."
    
    # Greetings
    if 'hi' in user or 'hello' in user or 'hey' in user:
        return "Hey there! Good to see you here!\nHow are you?"
    
    elif 'am good' in user or 'good' in user or 'fine' in user:
        return "That's Great!\nI can assist you with providing information about colleges near you!\nTo continue enter 'ok'"
    
    elif 'how are you' in user or "how r u" in user:
        return "Am doing good, Thanks for asking.\nI can assist you with providing information about colleges near you!\nTo continue enter 'ok'"
    
    elif 'ok' in user or 'okay' in user:
        return "Good to go!\nEnter college name or the Area name to fetch the details!"
    
    # College search logic - ALL CONDITIONS CONVERTED
    elif 'university of madras' in user or 'chepauk' in user or 'triplicane' in user:
        return f"**University of Madras**\n\n{df.iloc[0].to_string()}"
    
    elif 'anna university' in user or 'guindy' in user:
        return f"**Anna University**\n\n{df.iloc[1].to_string()}"
    
    elif 'college of engineering' in user or 'guindy' in user:
        return f"**College of Engineering, Guindy**\n\n{df.iloc[2].to_string()}"
    
    elif 'madras christian college' in user or 'mcc' in user or 'east tambaram' in user:
        return f"**Madras Christian College**\n\n{df.iloc[3].to_string()}"
    
    elif 'loyola college' in user or 'nungambakkam' in user:
        return f"**Loyola College**\n\n{df.iloc[4].to_string()}"
    
    elif 'presidency college' in user or 'chepauk' in user:
        return f"**Presidency College**\n\n{df.iloc[5].to_string()}"
    
    elif "st. joseph's college" in user or 'cuddalore' in user:
        return f"**St. Joseph's College**\n\n{df.iloc[6].to_string()}"
    
    elif "women's christian college" in user or 'nungambakkam' in user:
        return f"**Women's Christian College**\n\n{df.iloc[7].to_string()}"
    
    elif 'ssn college of engineering' in user or 'kalavakkam' in user:
        return f"**SSN College of Engineering**\n\n{df.iloc[8].to_string()}"
    
    elif 'sri venkateswara college of engineering (svce)' in user or 'pennalur' in user or 'sriperumbadur' in user:
        return f"**Sri Venkateswara College of Engineering (SVCE)**\n\n{df.iloc[9].to_string()}"
    
    elif 'srm institute of science and technology (main campus)' in user or 'srm' in user or 'kattankulathur' in user:
        return f"**SRM Institute of Science and Technology (Main Campus)**\n\n{df.iloc[10].to_string()}"
    
    elif 'vellore institute of technology (vit chennai)' in user or 'kelambakkam' in user or 'vandalur' in user:
        return f"**Vellore Institute of Technology (VIT Chennai)**\n\n{df.iloc[11].to_string()}"
    
    elif 'saveetha engineering college (saveetha university)' in user or 'thandalam' in user:
        return f"**Saveetha Engineering College (Saveetha University)**\n\n{df.iloc[12].to_string()}"
    
    elif "rajalakshmi engineering college (rec)" in user or 'rajalakshmi nagar' in user or 'thandalam' in user:
        return f"**Rajalakshmi Engineering College (REC)**\n\n{df.iloc[13].to_string()}"
    
    elif 'jeppiaar engineering college (jec)' in user or 'omr' in user or 'rajiv gandhi salai' in user:
        return f"**Jeppiaar Engineering College (JEC)**\n\n{df.iloc[14].to_string()}"
    
    elif 'chennai institute of technology (cit)' in user or 'kundrathur' in user:
        return f"**Chennai Institute of Technology (CIT)**\n\n{df.iloc[15].to_string()}"
    
    elif 'hindustan institute of technology and science' in user or 'hindustan' in user or 'omr' in user or 'padur' in user:
        return f"**Hindustan Institute of Technology and Science**\n\n{df.iloc[16].to_string()}"
    
    elif 'academy of maritime education and training' in user or 'ecr' in user or 'kanathur' in user:
        return f"**Academy of Maritime Education and Training**\n\n{df.iloc[17].to_string()}"
    
    elif 'dr. mgr educational and research institute' in user or 'maduravoyil' in user:
        return f"**Dr. MGR Educational and Research Institute**\n\n{df.iloc[18].to_string()}"
    
    elif 'b. s. abdur rahman crescent institute of science and technology' in user or 'crescent' in user or 'vandalur' in user:
        return f"**B.S. Abdur Rahman Crescent Institute of Science and Technology**\n\n{df.iloc[19].to_string()}"
    
    elif 'stanley medical college' in user or 'broadway' in user:
        return f"**Stanley Medical College**\n\n{df.iloc[20].to_string()}"
    
    elif 'madras medical college' in user or 'park town' in user:
        return f"**Madras Medical College**\n\n{df.iloc[21].to_string()}"
    
    elif 'ethiraj college for women' in user or 'egmore' in user:
        return f"**Ethiraj College for Women**\n\n{df.iloc[22].to_string()}"
    
    elif 'dg vaishnav college' in user or 'saidapet' in user:
        return f"**D G Vaishnav College**\n\n{df.iloc[23].to_string()}"
    
    elif 'mop vaishnav college for women' in user or 'nungambakkam' in user:
        return f"**MOP Vaishnav College for Women**\n\n{df.iloc[24].to_string()}"
    
    elif 'the new college' in user or 'royapettah' in user:
        return f"**The New College**\n\n{df.iloc[25].to_string()}"
    
    elif 'vels institute of science' in user or 'pallavaram' in user:
        return f"**Vels Institute of Science**\n\n{df.iloc[26].to_string()}"
    
    elif 'sathyabama institute of science and technology' in user or 'omr' in user:
        return f"**Sathyabama Institute of Science and Technology**\n\n{df.iloc[27].to_string()}"
    
    elif 'indian institute of technology madras (iitm)' in user or 'adyar' in user:
        return f"**Indian Institute of Technology Madras (IITM)**\n\n{df.iloc[28].to_string()}"
    
    elif 'national institute of fashion technology' in user or 'taramani' in user:
        return f"**National Institute of Fashion Technology**\n\n{df.iloc[29].to_string()}"
    
    elif 'srm institute of science and technology' in user or 'ramapuram' in user:
        return f"**SRM Institute of Science and Technology (Ramapuram)**\n\n{df.iloc[30].to_string()}"
    
    elif 'a m jain college' in user or 'meenambakkam' in user or 'minambakkam' in user:
        return f"**A M Jain College**\n\n{df.iloc[31].to_string()}"
    
    elif 'bharath institute of higher education and research' in user or 'selaiyur' in user:
        return f"**Bharath Institute of Higher Education and Research**\n\n{df.iloc[32].to_string()}"
    
    elif 'srm institute of science and technology' in user or 'vadapalani' in user:
        return f"**SRM Institute of Science and Technology (Vadapalani)**\n\n{df.iloc[33].to_string()}"
    
    elif 'madras institute of technology(mit)' in user or 'chrompet' in user:
        return f"**Madras Institute of Technology (MIT)**\n\n{df.iloc[34].to_string()}"
    
    else:
        return "Failed to fetch the results!\nTry entering other Name or any other Location"


# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get response
    response = chatbot_response(prompt)
    
    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Refresh
    st.rerun()


# Clear chat button
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi Buddy! I can help you find information about colleges in Chennai. How can I assist you today?"}
    ]
    st.rerun()