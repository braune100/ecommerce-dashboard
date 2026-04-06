# ecommerce-dashboard
This project is an interactive E-commerce Sales Dashboard built using Python and Streamlit. 
It analyzes transactional data (~97k rows) to provide insights into revenue, customer behavior, product performance, and geographic trends.  
The dashboard enables dynamic filtering and highlights key business metrics to support data-driven decision-making.
🚀 Live Demo

🔗 https://ecommerce-dashboard2.streamlit.app

🛠️ Tools & Technologies

Python
Pandas
Streamlit

📁 Dataset
The dataset includes:

Invoice transactions
Product descriptions
Customer IDs
Countries
Quantity and pricing data

📈 Features
🔹 Key Performance Indicators (KPIs)

Total Revenue
Total Orders
Average Order Value
Unique Customers
Returns Value

🔹 Interactive Filters

Date range selection
Country selection

🔹 Visualizations

Revenue over time
Top products by revenue
Revenue by country
Monthly trends
Order value distribution

🔹 Advanced Analytics

Customer segmentation (High / Medium / Low value)
Top customers analysis
Returns handling (negative quantities)

🔹 Additional Features

Data export (download filtered dataset)

🧠 Key Insights

A small number of customers contribute significantly to total revenue
Certain products dominate overall sales performance
Sales trends vary across countries and time periods
Returns impact net revenue and must be considered in analysis

▶️ How to Run Locally

git clone https://github.com/braune100/ecommerce-dashboard.git
cd ecommerce-dashboard
pip install -r requirements.txt
streamlit run app.py

📌 Future Improvements

Customer lifetime value (CLV)
Cohort analysis
Sales forecasting (Machine Learning)
UI/UX enhancements

👤 Author

Bruno Silveira
