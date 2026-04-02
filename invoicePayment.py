from typing import List, Dict
def compute(payment:str, invoices:List[str]):
    """
    payment=""
    Input Example: payment = "payment5,1000,Paying off: invoiceC" invoices = [ "invoiceA,2024-01-01,100", "invoiceB,2024-02-01,200", "invoiceC,2023-01-30,1000" ]
    Expected Output: payment5 pays off 1000 for invoiceC due on 2023-01-30
    """
    payment_data=payment.split(",")
    payment_id=payment_data[0].strip()
    payment_amount=int(payment_data[1].strip())
    memo=payment_data[2].strip()
    invoice_id=extract_invoic_id_from_memo(memo)
    if not invoice_id:
        return f"Error:Could not extract invoce ID from {memo}" 
    invoice_data=find_invoice_data(invoice_id, invoices)
    if not invoice_data:
        return f"Error: {invoice_id} not found"
    return format_reconcilation(payment_id, payment_amount, invoice_data)

def extract_invoic_id_from_memo(memo):
    if "Paying off:" in memo:
        invoice_id=memo.split("Paying off:")[1].strip()
        return invoice_id
        # return memo.split("Paying off:")[0].strip()
    # else:
    #     return f"Error:Could find memo {memo}"
def find_invoice_data(invoice_id, invoices):
    for invoice_str in invoices:
        # invoice_id_in=i.[0].strip()
        parts=invoice_str.split(",")
        inv_id=parts[0].strip()
        if inv_id==invoice_id:
            return {
                "invoice_id":inv_id,
                "due_date":parts[1].strip(),
                "amount_due":int(parts[2].strip())
            }
    return None 
def format_reconcilation(payment_id, payment_amount, invoice_data):
    return f"{payment_id} pays off {payment_amount} for {invoice_data["invoice_id"]} due on {invoice_data["due_date"]} "

#Test case
payment="payment5,10,Paying off:invoiceC"
invoices=["invoiceC, 2026-17-28,100"]
print(compute(payment, invoices))


def run_all_tests():
    """
    Comprehensive test suite to demonstrate during interview.
    """
    print("=" * 80)
    print("STRIPE INVOICE RECONCILIATION - TEST SUITE")
    print("=" * 80)
    
    # ========================================================================
    # TEST 1: Basic Example (Given in Problem)
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 1: Basic Example")
    print("=" * 80)
    
    payment = "payment5,1000,Paying off: invoiceC"
    invoices = [
        "invoiceA,2024-01-01,100",
        "invoiceB,2024-02-01,200",
        "invoiceC,2023-01-30,1000"
    ]
    
    result = reconcile_payment(payment, invoices)
    expected = "payment5 pays off 1000 for invoiceC due on 2023-01-30"
    
    print(f"\nInput:")
    print(f"  Payment: {payment}")
    print(f"  Invoices: {len(invoices)} invoices")
    
    print(f"\nOutput:")
    print(f"  {result}")
    
    print(f"\nExpected:")
    print(f"  {expected}")
    
    print(f"\n✅ Test 1: {'PASS' if result == expected else 'FAIL'}")
    
    # ========================================================================
    # TEST 2: Invoice Not Found
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 2: Invoice Not Found")
    print("=" * 80)
    
    payment = "payment1,500,Paying off: invoiceZ"
    invoices = ["invoiceA,2024-01-01,100"]
    
    result = reconcile_payment(payment, invoices)
    
    print(f"\nInput:")
    print(f"  Payment: {payment}")
    print(f"  Invoices: {invoices}")
    
    print(f"\nOutput:")
    print(f"  {result}")
    
    print(f"\n✅ Test 2: {'PASS' if 'Error' in result else 'FAIL'}")
    
    # ========================================================================
    # TEST 3: Multiple Invoices, Find Correct One
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 3: Multiple Invoices")
    print("=" * 80)
    
    payment = "payment10,5000,Paying off: invoice5"
    invoices = [
        "invoice1,2024-01-01,1000",
        "invoice2,2024-02-01,2000",
        "invoice3,2024-03-01,3000",
        "invoice4,2024-04-01,4000",
        "invoice5,2024-05-01,5000",
    ]
    
    result = reconcile_payment(payment, invoices)
    
    print(f"\nInput:")
    print(f"  Payment: {payment}")
    print(f"  Invoices: {len(invoices)} invoices")
    
    print(f"\nOutput:")
    print(f"  {result}")
    
    print(f"\n✅ Test 3: {'PASS' if 'invoice5' in result and '2024-05-01' in result else 'FAIL'}")
    
    # ========================================================================
    # TEST 4: Edge Case - Empty Invoice List
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 4: Empty Invoice List")
    print("=" * 80)
    
    payment = "payment99,100,Paying off: invoiceX"
    invoices = []
    
    result = reconcile_payment(payment, invoices)
    
    print(f"\nInput:")
    print(f"  Payment: {payment}")
    print(f"  Invoices: {invoices}")
    
    print(f"\nOutput:")
    print(f"  {result}")
    
    print(f"\n✅ Test 4: {'PASS' if 'Error' in result or 'not found' in result else 'FAIL'}")
    
    # ========================================================================
    # TEST 5: Amount Validation
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 5: Amount Mismatch (Partial Payment)")
    print("=" * 80)
    
    payment = "payment20,500,Paying off: invoiceX"
    invoices = ["invoiceX,2024-06-01,1000"]
    
    result_dict = reconcile_payment_with_validation(payment, invoices)
    
    print(f"\nInput:")
    print(f"  Payment: {payment}")
    print(f"  Payment Amount: $5.00")
    print(f"  Invoice Amount Due: $10.00")
    
    print(f"\nOutput:")
    print(f"  Status: {result_dict['status']}")
    print(f"  Message: {result_dict['message']}")
    if 'difference' in result_dict:
        print(f"  Difference: ${result_dict['difference'] / 100:.2f}")
    
    print(f"\n✅ Test 5: {'PASS' if result_dict['status'] == 'PARTIAL' else 'FAIL'}")
    
    # ========================================================================
    # TEST 6: Overpayment
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 6: Overpayment")
    print("=" * 80)
    
    payment = "payment30,2000,Paying off: invoiceY"
    invoices = ["invoiceY,2024-07-01,1000"]
    
    result_dict = reconcile_payment_with_validation(payment, invoices)
    
    print(f"\nInput:")
    print(f"  Payment: {payment}")
    print(f"  Payment Amount: $20.00")
    print(f"  Invoice Amount Due: $10.00")
    
    print(f"\nOutput:")
    print(f"  Status: {result_dict['status']}")
    print(f"  Message: {result_dict['message']}")
    if 'difference' in result_dict:
        print(f"  Overpayment: ${result_dict['difference'] / 100:.2f}")
    
    print(f"\n✅ Test 6: {'PASS' if result_dict['status'] == 'OVERPAID' else 'FAIL'}")
    
    # ========================================================================
    # TEST 7: Batch Processing
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 7: Batch Processing Multiple Payments")
    print("=" * 80)
    
    payments = [
        "payment1,100,Paying off: inv1",
        "payment2,200,Paying off: inv2",
        "payment3,300,Paying off: inv3"
    ]
    
    invoices = [
        "inv1,2024-01-01,100",
        "inv2,2024-02-01,200",
        "inv3,2024-03-01,300"
    ]
    
    results = reconcile_multiple_payments(payments, invoices)
    
    print(f"\nInput:")
    print(f"  {len(payments)} payments")
    print(f"  {len(invoices)} invoices")
    
    print(f"\nOutput:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")
    
    print(f"\n✅ Test 7: {'PASS' if len(results) == 3 else 'FAIL'}")
    
    # ========================================================================
    # TEST 8: Special Characters in Memo
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 8: Special Characters in Invoice ID")
    print("=" * 80)
    
    payment = "payment40,750,Paying off: invoice-ABC-123"
    invoices = ["invoice-ABC-123,2024-08-01,750"]
    
    result = reconcile_payment(payment, invoices)
    
    print(f"\nInput:")
    print(f"  Payment: {payment}")
    
    print(f"\nOutput:")
    print(f"  {result}")
    
    print(f"\n✅ Test 8: {'PASS' if 'invoice-ABC-123' in result else 'FAIL'}")
    
    # ========================================================================
    # Summary
    # ========================================================================
    print("\n" + "=" * 80)
    print("✅ ALL TESTS COMPLETE")
    print("=" * 80)


# ============================================================================
# MAIN FUNCTION FOR INTERVIEW
# ============================================================================

if __name__ == "__main__":
    # Run comprehensive test suite
    run_all_tests()
    
    # ========================================================================
    # Interview Tips
    # ========================================================================
    print("\n" + "=" * 80)
    print("INTERVIEW TIPS")
    print("=" * 80)
