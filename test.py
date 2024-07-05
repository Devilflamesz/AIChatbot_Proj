import pandas as pd

# Sample emails with their respective security classifications
data = {
    'email_text': [
        "This document contains highly sensitive information about project X, including confidential client data and proprietary technology details. Access is restricted to authorized personnel only.",
        "The following is a confidential client data for the current quarter analysis. Please do not share this information with anyone outside of the company.",
        "Details about the upcoming product release for internal distribution only. This information is not to be shared with external parties until the official launch date.",
        "Official memo regarding company policy changes, effective immediately. All employees are required to comply with the new policies.",
        "Top secret mission details for next month's operation, including classified intelligence and strategic plans. Eyes only for authorized personnel.",
        "Internal review notes for project Delta, including confidential project details and proprietary technology information.",
        "Public announcement for the new product launch, including marketing materials and press releases.",
        "Restricted access details for the internal server, including login credentials and access protocols.",
        "Official statement for media release, including company responses to recent events and crisis management protocols.",
        # Additional entries for each category
        "Confidential financial report for the last quarter, including sensitive financial data and proprietary business information.",
        "Meeting minutes from the executive board, including confidential discussions and strategic decisions.",
        "Classified details about defense contracts, including sensitive government information and proprietary technology details.",
        "Restricted document for senior management only, including confidential personnel information and proprietary business data.",
        "Official announcement about the company event, including event details and logistical information.",
        "Internal discussion on the new policies, including confidential feedback and suggestions from employees.",
        "Top secret files on the latest intelligence, including classified information and strategic plans. Eyes only for authorized personnel.",
        "The project is classified as confidential, and all team members are required to sign a non-disclosure agreement before accessing project materials.",
        "Restricted information for internal use only, including confidential company data and proprietary business information.",
        # More entries for diversity
        "Confidential memo about upcoming layoffs, including sensitive personnel information and proprietary business data.",
        "Top secret research findings on AI development, including classified information and proprietary intellectual property.",
        "Secret email discussing strategic acquisitions, including confidential company data and proprietary business information.",
        "Official notice regarding office relocation, including logistical information and company updates.",
        "Restricted document outlining IT security protocols, including sensitive information and access controls.",
        "Confidential proposal for new client engagement, including sensitive business strategies and potential partnership details.",
        "Top secret product roadmap for next year, including strategic product development plans and market insights.",
        "Confidential HR policy update, including changes to employee benefits and workplace policies.",
        "Official statement on environmental sustainability goals, including corporate initiatives and sustainability targets.",
        # Additional entries
        "Restricted budget allocation details, including financial plans and investment strategies.",
        "Confidential marketing campaign strategy, including target audience analysis and campaign metrics.",
        "Top secret research grant application, including project objectives and anticipated research outcomes.",
        "Official company performance review presentation, including financial performance highlights and strategic goals achievement.",
        "Secret memo on employee benefits update, including changes to employee compensation and benefits packages.",
        "Confidential supply chain optimization plan, including supply chain analysis and efficiency improvement strategies.",
        "Top secret competitive analysis report, including market intelligence and competitor strategies assessment.",
        "Official corporate social responsibility initiative, including community engagement programs and sustainability efforts.",
        "Restricted legal advisory document, including legal advice and compliance recommendations.",
        # More entries for variety
        "Confidential prototype design specifications, including product design details and development timeline.",
        "Top secret executive compensation details, including executive compensation structure and performance-based incentives.",
        "Secret audit report findings, including audit results and recommendations for improvement.",
        "Official public relations strategy outline, including media relations strategy and crisis communication plan.",
        "Restricted intellectual property protection strategy, including IP protection measures and patent portfolio management.",
        "Confidential R&D project update, including research progress and project timeline updates.",
        "Top secret government contract negotiations, including contract details and negotiation strategies.",
        "Official customer satisfaction survey results, including survey responses and customer feedback analysis.",
        "Restricted partner collaboration agreement, including partnership terms and collaboration guidelines.",
        # Additional entries
        "Confidential secret prototype design specifications, including confidential product design details and development timeline.",
        "Top secret executive compensation details, including executive compensation structure and performance-based incentives.",
        "Secret audit report findings, including audit results and recommendations for improvement.",
        "Official public relations strategy outline, including media relations strategy and crisis communication plan.",
        "Restricted intellectual property protection strategy, including IP protection measures and patent portfolio management.",
        "Confidential R&D project update, including research progress and project timeline updates.",
        "Top secret government contract negotiations, including contract details and negotiation strategies.",
        "Official customer satisfaction survey results, including survey responses and customer feedback analysis.",
        "Restricted partner collaboration agreement, including partnership terms and collaboration guidelines.",
    ],
    'label': [
        "Confidential",  # Question 1: Yes
        "Official (Closed)",  # Question 4: No
        "Official (Open)",  # Question 5: Full
        "Top Secret",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Secret",  # Question 3: Yes
        "Official (Open)",  # Question 5: Full
        "Restricted",  # Question 3: Yes
        "Official (Closed)",  # Question 4: No
        # Additional entries
        "Confidential",  # Question 1: Yes
        "Official (Closed)",  # Question 4: No
        "Top Secret",  # Question 1: Yes
        "Restricted",  # Question 3: Yes
        "Official (Open)",  # Question 5: Full
        "Official (Open)",  # Question 5: Full
        "Top Secret",  # Question 1: Yes
        "Confidential",  # Question 1: Yes
        "Restricted",  # Question 3: Yes
        # More labels
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Secret",  # Question 3: No
        "Official (Open)",  # Question 5: Partial
        "Restricted",  # Question 3: Yes
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Confidential",  # Question 1: Yes
        "Official (Open)",  # Question 5: Full
        # Additional labels
        "Restricted",  # Question 3: Yes
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Official (Open)",  # Question 5: Partial
        "Secret",  # Question 3: No
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Official (Open)",  # Question 5: Full
        "Restricted",  # Question 3: Yes
        # More labels
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Secret",  # Question 3: No
        "Official (Open)",  # Question 5: Partial
        "Restricted",  # Question 3: Yes
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Official (Open)",  # Question 5: Full
        "Restricted",  # Question 3: Yes
        # Additional entries
        "Restricted",  # Question 3: Yes
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Official (Open)",  # Question 5: Partial
        "Secret",  # Question 3: No
        "Confidential",  # Question 1: Yes
        "Top Secret",  # Question 1: Yes
        "Official (Open)",  # Question 5: Full
        "Restricted",  # Question 3: Yes
    ]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv('email_classification_dataset.csv', index=False)

print("Dataset saved successfully.")
