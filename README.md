# CBI Enforcement Actions Tracker

A data analysis project tracking all enforcement actions taken by the 
Central Bank of Ireland (CBI) from 2022 to 2025.

## What This Project Does

- Compiles 12 CBI enforcement actions from public PDF settlement notices
- Analyses fine amounts, breach categories and institution types
- Builds 4 Python charts showing trends and patterns
- Exports clean data for Power BI dashboard

## Key Findings

- Total fines collected: €123,302,259
- Largest fine: €83,300,000 — AIB tracker mortgage scandal
- Smallest fine: €8,400 — Kerry Insurance Group (Fitness & Probity)
- Most common breach: AML Transaction Monitoring (3 cases)
- 8 different institution types sanctioned
- 9 different regulations breached

## Breach Categories Found

| Breach Type | Cases | Total Fines |
|---|---|---|
| AML | 3 | €23,320,007 |
| Consumer Protection | 1 | €83,300,000 |
| Governance | 2 | €4,033,512 |
| Outsourcing | 1 | €10,780,000 |
| Market Abuse | 1 | €1,225,000 |
| Safeguarding | 1 | €324,240 |
| Reporting Failure | 1 | €192,500 |
| Investor Disclosure | 1 | €117,600 |
| Fitness & Probity | 1 | €8,400 |

## Tools Used

- Python (pandas, matplotlib)
- Microsoft Power BI
- Data source: centralbank.ie

## Files in This Repository

- analysis.py — Python analysis script
- cbi_powerbi.csv — Clean dataset
- chart1_fines_per_year.png
- chart2_by_institution.png
- chart3_breach_types.png
- chart4_actions_per_year.png

## Key Insight for Compliance Professionals

In every AML case in this dataset the firm knew about 
the problem long before telling the CBI. The CBI 
consistently treated that delay as an aggravating 
factor and increased the fine as a result.

## Data Source

All data sourced from public settlement notices on 
centralbank.ie/news-media/legal-notices/enforcement-actions
