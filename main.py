import streamlit as st
from PIL import Image

# Basic App Setup
st.set_page_config(page_title="Collins Mutai's CV", page_icon=":wave:")

# Sidebar for Download and Contact Info
st.sidebar.title("Collins Mutai")
st.sidebar.image("https://avatars.githubusercontent.com/u/0000000?v=4", width=150)  # Replace with actual profile image link or remove this line if not needed
st.sidebar.write("📍 Ngong, Kenya")
st.sidebar.write("📧 [kipkorircmutai@gmail.com](mailto:kipkorircmutai@gmail.com)")
st.sidebar.write("📞 +254 799471473")
st.sidebar.write("[GitHub: KipkorirC](https://github.com/KipkorirC)")

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

# Main Content
st.title("Collins Mutai")
st.write("An energetic and enthusiastic service professional with a passion for data science and computer vision.")
st.write("---")

# Summary Section
st.header("🎯 Summary")
st.write("""
    Passionate IT professional with practical experience in data science and computer vision. Demonstrated expertise in
    designing and implementing software solutions for complex problems. Committed to continuous learning and delivering 
    high-quality results.
""")

# Certificates
st.header("📜 Certificates")
st.write("- Data Analysis and Visualization in Python")

# Education
st.header("🎓 Education")
st.write("**St. Paul's University** - Bachelor of Science in Computer Science")
st.write("Limuru, Kenya")

# Professional Experience
st.header("💼 Professional Experience")

st.subheader("EGIS Foundation")
st.write("**Finalist** (Team up for climate change international competition)")
st.write("""
    - Created a mathematical model to calculate rainwater harvesting potential based on roof characteristics.
    - Developed a simulation program to track tank water balance, incorporating roof runoff and user consumption.
    - Visualized results to determine optimum tank capacity balancing cost and harvesting potential.
""")

st.subheader("Kenya Power and Electricity Company (KPLC)")
st.write("**Data Analyst**")
st.write("Mar 2024 – Jun 2024 | Nairobi, Kenya")
st.write("""
    - Analyzed and developed financial data dashboards.
    - Created live dashboards for smart meters in the field.
    - Troubleshooted and diagnosed network issues across the company.
    - Conducted on-site preventive maintenance and managed cable organization.
    - Provided client and customer service within the company.
""")

# Projects Section
st.header("🚀 Projects")

st.subheader("Rainwater Harvesting Simulation Project")
st.write("""
    - Developed a mathematical model to estimate rainwater harvesting potential based on roof characteristics.
    - Built a simulation tool to calculate water storage and consumption, tracking tank balance over time.
    - Visualized optimal tank capacities, balancing cost-efficiency and maximized water collection.
    - Enabled user-defined inputs to tailor simulations to varying environmental and structural conditions.
    - Finalist in the *Team Up for Climate Change* international competition, showcasing practical climate solutions.
    - Explore the live project here: [Majihaven - Rainwater Harvesting](https://majihaven.streamlit.app)
""")

st.subheader("Web Scraping Car Data (jiji.co.ke)")
st.write("""
    - Developed a custom ETL pipeline for scraping car data from **jiji.co.ke** using Python's **BeautifulSoup** library.
    - Designed and implemented an efficient data extraction, transformation, and loading process.
    - Managed dependencies using **Conda** to ensure a consistent development environment.
    - Dockerized the entire application for seamless deployment and scalability.
    - Integrated **Jenkins** for automating the data pipeline and continuous data flow.
    - Created insightful dashboards in **Tableau** and **Power BI** to visualize the scraped data.
    - Explore the live project here: [Web Scraping Car Data Project](https://your-link-to-web-scraping-project)
""")

# Skills
st.header("🔧 Skills")
st.write("""
    - **MS Office Suite:** PowerPoint, Excel, Teams, Word
    - **DevOps & Cloud:** Jenkins, Git & GitHub, Docker, Microsoft Azure, Azure DevOps
    - **Operating Systems:** Windows, macOS, Linux
    - **Web Development:** PHP, FastAPI, Streamlit, ASP.NET
    - **Programming Languages:** C/C++, Python, R
""")

# References
st.header("📇 References")
st.write("**Haron Samoei** - Engineer AMI, Kenya Power and Lighting Company")
st.write("📧 Hsamoei@kplc.co.ke | 📞 +254737380972")
st.write("**Fanon Ngetich** - Network Engineer, Kenya Power and Lighting Company")
st.write("📧 fanonngetich@kplc.co.ke | 📞 +254723568468")
st.write("**Anthony Sifuma** - Accountant - Telecoms Division, Kenya Power and Lighting Company")
st.write("📧 ASifuma@kplc.co.ke | 📞 +254726854763")
st.write("**Hafiz Nauman Yousaf** - Mentor, Egis Foundation")
st.write("📧 Hafiz.NAUMAN-YOUSAF@egis-group.com | 📞 +971504890358")
