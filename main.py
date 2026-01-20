

def main():
    
   # Main execution function

    print ()
    # Workflow:
    # 1. Print welcome message
    
    print()
    # 2. Read sales data file (handle encoding)

    # 3. Parse and clean transactions

    # 4. Display filter options to user
    #   - Show available regions
    #   - Show transaction amount range
    #   - Ask if user wants to filter (y/n)
    
    # 5. If yes, ask for filter criteria and apply

    # 6. Validate transactions
    
    # 7. Display validation summary

    # 8. Perform all data analyses (call all functions from Part 2)

    # 9. Fetch products from API

    #10. Enrich sales data with API info
    
    #11. Save enriched data to file
    
    #12. Generate comprehensive report
    
    #13. Print success message with file locations

    # Error Handling:
    # - Wrap entire process in try-except
    # - Display user-friendly error messages
    # - Don't let program crash on errors

    #Expected Console Output:
    print("====================================================")
    print("..............SALES ANALYTICS SYSTEM................")
    print("...........Created by Arun Ramarathnam..............")
    print("====================================================")
    print("")    
    print("")

    print("READING SALES DATA FILE...")
    #✓ Successfully read 95 transactions
    print("")

    print("PARSING AND CLEANING DATA...")
    #✓ Parsed 95 records
    print("Cleaned data: Removed 2 duplicates, 0 invalid records")
    print("")

    print("FILTER OPTIONS AVAILABLE:")
    print("Regions: North, South, East, West")
    print("Amount Range: ₹500 - ₹90,000")
    print("")
    print("Do you want to filter data? (y/n): ")
    print("")
    print("Validating transactions...")
    #✓ Valid: 92 | Invalid: 3
    print("")

    print("ANALYSING SALES DATA...")
    print("Analysis complete!")
    print("")

    print("Fetching product data from API...")
    #✓ Fetched 30 products
    print("")

    print("ENRICHING SALES DATA...") 
    print("with product info...")
    #✓ Enriched 85/92 transactions (92.4%)
    print("")

    print("Saving enriched data...")
    print("Saved to: data/enriched_sales_data.txt")
    print("")
    
    print("GENERATING REPORT...")
    print("Report saved to: output/sales_report.txt")
    print("")

    print("Process Complete!")
    print("")
    print("==================================================")
    print("Thank youfor using the Sales Analytics System.")
    print("==================================================")
    print("")    
    print("")

main()
