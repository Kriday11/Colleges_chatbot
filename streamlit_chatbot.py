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
        background-color: #008080;
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
    st.write("💡 **Try asking : **")
    st.write("- 'Anna University'")
    st.write("- 'Colleges in Guindy'")
    st.write("- '60----'")
    st.write("- 'SRM Institute'")


try:
    df = pd.read_csv("colleges_csvfile.csv", delimiter=',')
    st.sidebar.success(f"✅ Loaded {len(df)} colleges")
except Exception as e:
    st.error(f"CSV file error: {e}")
    df = pd.DataFrame()


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi Buddy!"}
    ]


def chatbot_response(user_input):
    user = user_input.lower()
    

    if df.empty:
        return "Database not loaded. Please check CSV file."
    
    
    if 'hi' in user or 'hello' in user or 'hey' in user:
        return "Hey there! Good to see you here!\nHow are you?"
    
    elif 'am good' in user or 'good' in user or 'fine' in user:
        return "That's Great!\nI can assist you with providing information about colleges near you!\nTo continue enter 'ok'"
    
    elif 'how are you' in user or "how r u" in user:
        return "Am doing good, Thanks for asking.\nI can assist you with providing information about colleges near you!\nTo continue enter 'ok'"
    
    elif 'ok' in user or 'okay' in user:
        return "Good to go!\nEnter college name or the Area name to fetch the details!"
    
   
    def format_college_info(college_row):
        info = f"**🏫 {college_row.get('Name', 'College')}**\n\n"
        
     
        fields = [
            ("📍 Address", college_row.get('Address', 'Not available')),
            ("📮 Pincode", college_row.get('Pincode', 'Not available')),
            ("🎓 Type", college_row.get('Type', 'Not available')),
            ("🏙️ City", college_row.get('City', 'Not available')),
            ("🗺️ State", college_row.get('State', 'Not available'))
        ]
        
        for label, value in fields:
            if pd.notna(value):  
                info += f"• **{label}:** {value}\n"
        
        info += f"\n✅ **Total colleges in database:** {len(df)}"
        return info
    
    
    if 'university of madras' in user or 'chepauk' in user or 'triplicane' in user or '600005' in user:
        return format_college_info(df.iloc[0])
    
    elif 'anna university' in user or 'guindy' in user or '600025' in user:
        return format_college_info(df.iloc[1])
    
    elif 'college of engineering' in user or 'guindy' in user or '600025' in user:
        return format_college_info(df.iloc[2])
    
    elif 'madras christian college' in user or 'mcc' in user or 'east tambaram' in user or '600059' in user:
        return format_college_info(df.iloc[3])
    
    elif 'loyola college' in user or 'nungambakkam' in user or '600034' in user:
        return format_college_info(df.iloc[4])
    
    elif 'presidency college' in user or 'chepauk' in user or '600005' in user:
        return format_college_info(df.iloc[5])
    
    elif "st. joseph's college" in user or 'cuddalore' in user or '600001' in user:
        return format_college_info(df.iloc[6])
    
    elif "women's christian college" in user or 'nungambakkam' in user or 'wcc' in user or '600006' in user:
        return format_college_info(df.iloc[7])
    
    elif 'ssn college of engineering' in user or 'kalavakkam' in user or 'ssn' in user or '603110' in user:
        return format_college_info(df.iloc[8])
    
    elif 'sri venkateswara college of engineering' in user or 'svce' in user or 'pennalur' in user or 'sriperumbadur' in user or 'sriperumbadur' in user or '602117' in user:
        return format_college_info(df.iloc[9])
    
    elif 'srm institute of science and technology (main campus)' in user or 'srm' in user or 'kattankulathur' in user or '603203' in user:
        return format_college_info(df.iloc[10])
    
    elif 'vellore institute of technology' in user or 'vit' in user or 'kelambakkam' in user or 'vandalur' in user or '600127' in user:
        return format_college_info(df.iloc[11])
    
    elif 'saveetha engineering college' in user or 'saveetha university' in user or 'thandalam' in user or '602105' in user:
        return format_college_info(df.iloc[12])
    
    elif "rajalakshmi engineering college (rec)" in user or 'rajalakshmi nagar' in user or 'thandalam' in user or '602105' in user:
        return format_college_info(df.iloc[13])
    
    elif 'jeppiaar engineering college' in user or 'omr' in user or 'rajiv gandhi salai' in user or '600119' in user:
        return format_college_info(df.iloc[14])
    
    elif 'chennai institute of technology (cit)' in user or 'cit' in user or 'kundrathur' in user or '600069' in user:
        return format_college_info(df.iloc[15])
    
    elif 'hindustan institute of technology and science' in user or 'hindustan' in user or 'omr' in user or 'padur' in user or '603103' in user:
        return format_college_info(df.iloc[16])
    
    elif 'academy of maritime education and training' in user or 'amet' in user or 'ecr' in user or 'kanathur' in user or '603112' in user:
        return format_college_info(df.iloc[17])
    
    elif 'dr. mgr educational and research institute' in user or 'mgr' in user or 'maduravoyil' in user or '600095' in user:
        return format_college_info(df.iloc[18])
    
    elif 'b. s. abdur rahman crescent institute of science and technology' in user or 'crescent' in user or 'vandalur' in user or '600048' in user:
        return format_college_info(df.iloc[19])
    
    elif 'stanley medical college' in user or 'broadway' in user or '600001' in user:
        return format_college_info(df.iloc[20])
    
    elif 'madras medical college' in user or 'park town' in user or '600003' in user:
        return format_college_info(df.iloc[21])
    
    elif 'ethiraj college for women' in user or 'egmore' in user or '600008' in user:
        return format_college_info(df.iloc[22])
    
    elif 'dg vaishnav college' in user or 'saidapet' in user or '600015' in user:
        return format_college_info(df.iloc[23])
    
    elif 'mop vaishnav college for women' in user or 'nungambakkam' in user or '600034' in user:
        return format_college_info(df.iloc[24])
    
    elif 'the new college' in user or 'royapettah' in user or '600014' in user:
        return format_college_info(df.iloc[25])
    
    elif 'vels institute of science' in user or 'pallavaram' in user or 'vels' in user or '600117' in user:
        return format_college_info(df.iloc[26])
    
    elif 'sathyabama institute of science and technology' in user or 'sathyabama' in user or 'omr' in user or '600119' in user:
        return format_college_info(df.iloc[27])
    
    elif 'indian institute of technology madras (iitm)' in user or 'iit' in user or 'iitm' in user or 'adyar' in user or '600036' in user:
        return format_college_info(df.iloc[28])
    
    elif 'national institute of fashion technology' in user or 'taramani' in user or '600113' in user:
        return format_college_info(df.iloc[29])
    
    elif 'srm institute of science and technology' in user or 'ramapuram' in user or '600089' in user:
        return format_college_info(df.iloc[30])
    
    elif 'a m jain college' in user or 'meenambakkam' in user or 'minambakkam' in user or '600061' in user:
        return format_college_info(df.iloc[31])
    
    elif 'bharath institute of higher education and research' in user or 'selaiyur' in user or '600073' in user:
        return format_college_info(df.iloc[32])
    
    elif 'srm institute of science and technology' in user or 'vadapalani' in user or '600026' in user:
        return format_college_info(df.iloc[33])
    
    elif 'madras institute of technology' in user or 'mit' in user or 'chrompet' in user or '600044' in user:
        return format_college_info(df.iloc[34])

    elif 'gurunanak' in user or 'velachery' in user or 'gnc' in user or 'guru nanak college' in user or '600042' in user:
        return format_college_info(df.iloc[35])

    elif 'stella maris college' in user or 'stella maris' in user or 'gopalapuram' in user or 'poes garden' in user or '600086' in user:
        return format_college_info(df.iloc[36])

    elif 'sri muthukumaran institute of technology' in user or 'smit' in user or 'kundrathur' in user or 'mangadu' in user or '600069' in user:
        return format_college_info(df.iloc[37])

        
    else:
        return "❌ Failed to fetch the results!\n\n💡 **Try asking about:**\n• 'Anna University'\n• 'Colleges in Guindy'\n• 'SRM Institute'"


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Type your message here..."):
   
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    
    response = chatbot_response(prompt)
    
   
    with st.chat_message("assistant"):
        st.markdown(response)
   
    st.session_state.messages.append({"role": "assistant", "content": response})
    

if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi Buddy! I can help you find information about colleges in Chennai. How can I assist you today?"}
    ]
    st.rerun()  

