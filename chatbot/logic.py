import pandas as pd

df = pd.read_excel("data/financials.xlsx")



def get_financial_info(company, query):
    try:
        company_data = df[df['Company'].str.lower() == company.lower()].sort_values(by="Year", ascending=False)
        latest = company_data.iloc[0]

        if "revenue" in query:
            return f"{company}'s total revenue in {latest['Year']} was {latest['Revenue']}."
        elif "net income" in query:
            return f"{company}'s net income in {latest['Year']} was {latest['Net Income']}."
        elif "assets" in query:
            return f"{company} had total assets worth {latest['Total Assets']} in {latest['Year']}."
        elif "liabilities" in query:
            return f"{company}'s liabilities in {latest['Year']} were {latest['Liabilities']}."
        elif "cash flow" in query:
            return f"{company}'s cash flow from operating activities was {latest['Cash Flow']} in {latest['Year']}."
        else:
            return "I can only answer questions about revenue, net income, assets, liabilities, or cash flow."

    except Exception as e:
        return "Sorry, I couldn’t find information for that query."
