"""
PDF QUALITY AUDITOR
Checks for graphic collisions, page fitting, and layout issues
"""
import os
import pymupdf
import glob


def audit_pdf(path):
    """Audit a single PDF for quality issues"""
    issues = []
    
    try:
        # Open PDF
        doc = pymupdf.open(path)
        
        # Check page count
        if doc.page_count < 3:
            issues.append(f"Low page count: {doc.page_count}")
        
        # Check each page
        for page_num in range(min(5, doc.page_count)):  # Check first 5 pages for speed
            page = doc[page_num]
            
            # Check for text (cover page might have less text)
            text = page.get_text()
            if page_num == 0:
                # Cover page checks
                if "EXPLOITS UNIVERSITY" not in text.upper():
                    issues.append(f"Page {page_num+1}: Missing 'EXPLOITS UNIVERSITY'")
                if "BICT 3202" not in text.upper():
                    issues.append(f"Page {page_num+1}: Missing 'BICT 3202'")
                if "WEEK" not in text.upper():
                    issues.append(f"Page {page_num+1}: Missing 'WEEK'")
            else:
                # Body page checks
                if len(text.strip()) < 50:
                    issues.append(f"Page {page_num+1}: Very little text (possible layout issue)")
                if len(text) > 4000:
                    issues.append(f"Page {page_num+1}: Very dense text ({len(text)} chars)")
            
            # Check for images
            images = page.get_images()
            if len(images) > 0 and len(text.strip()) < 100 and page_num > 0:
                issues.append(f"Page {page_num+1}: Potential image/text collision (low text, has images)")
        
        doc.close()
    except Exception as e:
        issues.append(f"Error opening PDF: {e}")
    
    return issues


def audit_all_pdfs():
    """Audit all PDFs in output folder"""
    pdf_files = glob.glob("/home/user/OOP-MODULE/output/**/*.pdf", recursive=True)
    
    print("="*70)
    print("PDF QUALITY AUDIT")
    print("="*70)
    
    all_issues = {}
    
    for pdf_path in pdf_files:
        week = os.path.basename(os.path.dirname(pdf_path))
        filename = os.path.basename(pdf_path)
        
        print(f"\nAuditing: {pdf_path}")
        issues = audit_pdf(pdf_path)
        
        if issues:
            print(f"  ✗ Found {len(issues)} issues:")
            for issue in issues:
                print(f"    - {issue}")
            all_issues[pdf_path] = issues
        else:
            print(f"  ✓ No issues found")
    
    print("\n" + "="*70)
    print("AUDIT SUMMARY")
    print("="*70)
    print(f"Total PDFs: {len(pdf_files)}")
    print(f"PDFs with issues: {len(all_issues)}")
    
    if all_issues:
        print("\nIssues found in:")
        for path, issues in all_issues.items():
            print(f"\n{path}:")
            for issue in issues:
                print(f"  - {issue}")
    else:
        print("\n✓ ALL PDFs PASSED QUALITY CHECK")
    
    return len(all_issues) == 0


if __name__ == "__main__":
    import sys
    success = audit_all_pdfs()
    sys.exit(0 if success else 1)
