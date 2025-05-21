import streamlit as st
from PIL import Image

# Basic App Setup
st.set_page_config(page_title="Collins Mutai's CV", page_icon=":wave:")

# Sidebar for Download and Contact Info
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #292929;
        color: #FFFFFF;
    }
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sidebar-content a {
        color: #1e90ff;
        text-decoration: none;
    }
    .sidebar-content a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown('<div class="sidebar-title">Collins Mutai</div>', unsafe_allow_html=True)
st.sidebar.image("https://avatars.githubusercontent.com/u/0000000?v=4", width=150)  # Replace with actual profile image link or remove this line if not needed
st.sidebar.write("📍 Ngong, Kenya")
st.sidebar.write("📧 [kipkorircmutai@gmail.com](mailto:kipkorircmutai@gmail.com)")
st.sidebar.write("📞 +254 799471473")
st.sidebar.write("[GitHub: KipkorirC](https://github.com/KipkorirC)")
st.sidebar.write("[LinkedIn: Collins Kipkorir Mutai](https://www.linkedin.com/in/collins-kipkorir-mutai/)")

# Download CV Button in Sidebar
pdf_path = "./CV.pdf"  # Ensure the CV PDF is saved at this path in the same directory
try:
    with open(pdf_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        st.sidebar.download_button(
            label="📄 Download CV PDF",
            data=PDFbyte,
            file_name="Collins_Mutai_CV.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.sidebar.error("CV PDF file not found. Please ensure it is saved at './Collins_Mutai_CV.pdf'.")

# Main Content with Tabs
st.markdown(
    """
    <style>
    .stTabs [data-baseweb="tab"] {
        background-color: #292929;
        color: #A9A9A9;
        font-weight: bold;
        border-radius: 5px;
        margin-right: 20px;
        padding: 15px 30px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: #1e90ff;
        color: white;
    }

    .stTabs [aria-selected="true"] {
        background-color: #1e90ff;
        color: white;
    }

    .stTabs {
        position: sticky;
        top: 0;
        z-index: 10;
        background-color: #292929;
        padding: 10px 0;
    }

    .stMarkdown h1 {
        margin-top: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Collins Mutai")
st.write("An energetic and enthusiastic service professional with practical experience in a fast-paced IT sector.")
st.write("---")

# Tabs for navigation
tabs = st.tabs(["Summary", "Experience", "Projects", "Skills", "References"])

# Tab 1: Summary
with tabs[0]:
    st.header("🎯 Summary")
    st.write(
        """
        Passionate IT professional with practical experience in data science and computer vision. Demonstrated ability to design,
        develop, and implement innovative software solutions to address complex problems. A passionate learner committed to 
        delivering high-quality results.
        """
    )

    st.header("📜 Certificates")
    st.write("- Data Analysis and Visualization in Python")
    st.write("- Artificial Intelligence Fundamentals (IBM)")

    st.header("🎓 Education")
    st.write("**St. Paul's University** - Bachelor of Science in Computer Science")
    st.write("Sep 2020 – Nov 2024 | Limuru, Kenya")

# Tab 2: Experience
with tabs[1]:
    st.header("💼 Professional Experience")

    st.subheader("Kenya Revenue Authority(KRA)")
    st.write("**ICT - Capacity and Monitoring Intern**")
    st.write("May 2025 – Present | Kenya")
    st.write(
        """
        - Monitored the performance, uptime, and health of IT infrastructure, identifying and escalating potential issues proactively.  
        - Assisted in analyzing usage trends and forecasting system capacity needs to support scalability and efficient resource allocation.  
        - Supported incident response by gathering logs, investigating root causes, and preparing detailed incident reports.  
        - Generated regular performance and capacity reports, highlighting key metrics, system trends, and areas for improvement.  
        - Maintained and optimized monitoring tools and dashboards to ensure accurate visualization of system health and performance data.
        """
    )

    st.subheader("KCB Bank Group")
    st.write("**Intern**")
    st.write("Sep 2024 – Present | Nairobi, Kenya")
    st.write(
        """
        - Conducted system testing and validation for new software deployments to ensure functionality and reliability.
        - Assisted in maintaining and updating databases, ensuring data accuracy and integrity for business operations.
        - Collaborated with teams to optimize IT processes by analyzing workflows and recommending system improvements.
        - Supported troubleshooting and resolution of technical issues, minimizing downtime and enhancing system performance.
        """
    )

    st.subheader("EGIS Foundation")
    st.write("**Finalist** (Team up for climate change international competition)")
    st.write("Jan 2024 – Apr 2024")
    st.write(
        """
        - Created a mathematical model to calculate the rainwater harvesting potential for a roof given its characteristics.
        - Used the model to create a simulation program to work with user input.
        - Implemented a program to track tank water balance, considering roof runoff and user consumption.
        - Generated and visualized simulation results and an optimum tank capacity which maximizes rainwater harvesting potential and minimizes cost.
        """
    )

    st.subheader("Kenya Power and Electricity Company (KPLC)")
    st.write("**IT Support**")
    st.write("Mar 2024 – Jun 2024 | Nairobi, Kenya")
    st.write(
        """
        - Analyzed and created dashboards for financial data.
        - Created live dashboards on live smart meters deployed in the field.
        - Troubleshot and diagnosed network issues across the company.
        - Conducted on-site preventive maintenance and cable management.
        - Provided client/customer service within the company.
        """
    )

# Tab 3: Projects
with tabs[2]:
    st.header("🚀 Projects")

    st.subheader("Rainwater Harvesting Simulation Project")
    st.write(
        """
        - Developed a mathematical model to estimate rainwater harvesting potential based on roof characteristics.
        - Built a simulation tool to calculate water storage and consumption, tracking tank balance over time.
        - Visualized optimal tank capacities, balancing cost-efficiency and maximized water collection.
        - Enabled user-defined inputs to tailor simulations to varying environmental and structural conditions.
        - Finalist in the *Team Up for Climate Change* international competition, showcasing practical climate solutions.
        - Explore the live project here: [Majihaven - Rainwater Harvesting](https://majihaven.streamlit.app)
        """
    )

    st.subheader("Web Scraping Car Data (jiji.co.ke)")
    st.write(
        """
        - Developed a custom ETL pipeline for scraping car data from **jiji.co.ke** using Python's **BeautifulSoup** library.
        - Designed and implemented an efficient data extraction, transformation, and loading process.
        - Managed dependencies using **Conda** to ensure a consistent development environment.
        - Dockerized the entire application for seamless deployment and scalability.
        - Integrated **Jenkins** for automating the data pipeline and continuous data flow.
        - Created insightful dashboards in **Tableau** and **Power BI** to visualize the scraped data.
        - Explore the live project here: [Web Scraping Car Data Project](https://your-link-to-web-scraping-project)
        """
    )

# Tab 4: Skills
with tabs[3]:
    st.header("🔧 Skills")
    st.write(
        """
        - **MS Office Suite:** PowerPoint, Excel, Teams, PowerApps
        - **DevOps & Cloud:** Jenkins, Git & GitHub, Docker, Microsoft Azure, Azure DevOps
        - **Programming Languages:** C/C++, Python, R
        - **Web Development:** PHP, FastAPI, Streamlit, ASP.NET
        - **Operating Systems:** Windows, macOS, Linux
        - **Monitoring Tools** Nagios and Nagvis, Grafana, Zabbix, Elastic Search, DCIM, Maglink
        """
    )

# Tab 5: References
with tabs[4]:
    st.header("📇 References")
    st.write("**Haron Samoei** - Engineer AMI (Advanced Metering Infrastructure), Kenya Power and Lighting Company")
    st.write("📧 Hsamoei@kplc.co.ke | 📞 +254737380972")
    st.write("**Fanon Ngetich** - Network Engineer, Kenya Power and Lighting Company")
    st.write("📧 fanonngetich@kplc.co.ke | 📞 +254723568468")
    st.write("**Anthony Sifuma** - Accountant - Telecoms Division, Kenya Power and Lighting Company")
    st.write("📧 ASifuma@kplc.co.ke | 📞 +254726854763")
    st.write("**Hafiz Nauman Yousaf** - Mentor, Egis Foundation")
    st.write("📧 Hafiz.yousaf.358@gmail.com | 📞 +971504890358")
