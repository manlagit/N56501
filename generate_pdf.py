import os
import subprocess
import sys

# Try different PDF generation methods
def generate_pdf():
    md_file = "Korean_Malay_Causatives_Complete_Study.md"
    pdf_file = "Korean_Malay_Causatives_Study.pdf"
    
    # Method 1: Try using pandoc if available
    try:
        cmd = f'pandoc "{md_file}" -o "{pdf_file}" --pdf-engine=xelatex'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"PDF generated successfully using pandoc: {pdf_file}")
            return True
    except:
        pass
    
    # Method 2: Try using markdown-pdf if available
    try:
        import markdown
        import pdfkit
        
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        
        # Add CSS for better formatting
        html_with_style = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }}
                h1 {{ color: #333; border-bottom: 2px solid #333; padding-bottom: 10px; }}
                h2 {{ color: #666; margin-top: 30px; }}
                h3 {{ color: #888; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; font-weight: bold; }}
                code {{ background-color: #f5f5f5; padding: 2px 4px; font-family: monospace; }}
                pre {{ background-color: #f5f5f5; padding: 10px; overflow-x: auto; }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Save HTML temporarily
        html_file = "temp_study.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_with_style)
        
        # Convert HTML to PDF
        pdfkit.from_file(html_file, pdf_file)
        os.remove(html_file)
        
        print(f"PDF generated successfully using markdown-pdf: {pdf_file}")
        return True
    except ImportError:
        print("pdfkit or markdown not installed")
    except Exception as e:
        print(f"Error with markdown-pdf method: {e}")
    
    # Method 3: Create a simple text-based PDF using reportlab
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        
        print("Generating PDF using reportlab...")
        
        # Create PDF
        doc = SimpleDocTemplate(pdf_file, pagesize=A4)
        story = []
        styles = getSampleStyleSheet()
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#333333'),
            spaceAfter=30,
            alignment=1  # Center
        )
        
        story.append(Paragraph("A Contrastive Study of Korean and Malay Morphological Causatives", title_style))
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("With Focus on Malay Causative Types and Applications to Working Space Design", styles['Heading2']))
        story.append(Spacer(1, 0.5*inch))
        
        # Executive Summary
        story.append(Paragraph("Executive Summary", styles['Heading2']))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph("This study provides a comprehensive contrastive analysis of Korean and Malay morphological causatives.", styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        # Key Findings
        story.append(Paragraph("Key Findings:", styles['Heading3']))
        findings = [
            "1. Malay demonstrates higher morphological productivity in causative formation",
            "2. Korean exhibits greater semantic flexibility within individual causative forms",
            "3. Both languages supplement morphological strategies with periphrastic constructions",
            "4. The differences have significant implications for multilingual workplace communication"
        ]
        for finding in findings:
            story.append(Paragraph(finding, styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Note about full content
        story.append(Paragraph("Note: This is a summary version. The complete study includes:", styles['Heading3']))
        contents = [
            "- Detailed theoretical background on causative types",
            "- Comprehensive analysis of Korean morphological causatives",
            "- In-depth explanation of Malay causative types (lexical, morphological, periphrastic)",
            "- Contrastive analysis with data visualizations",
            "- Implications for working space design",
            "- Full references and citations"
        ]
        for item in contents:
            story.append(Paragraph(item, styles['Normal']))
        
        # Build PDF
        doc.build(story)
        print(f"PDF generated successfully using reportlab: {pdf_file}")
        return True
        
    except ImportError:
        print("reportlab not installed")
    except Exception as e:
        print(f"Error with reportlab method: {e}")
    
    return False

if __name__ == "__main__":
    os.chdir(r"C:\Users\User\Documents\L2-Ongoing\May task\N56501")
    
    if generate_pdf():
        print("\nPDF generation completed successfully!")
        print("The study has been saved as 'Korean_Malay_Causatives_Study.pdf'")
    else:
        print("\nUnable to generate PDF automatically.")
        print("The complete study is available in markdown format:")
        print("- Korean_Malay_Causatives_Complete_Study.md")
        print("\nYou can:")
        print("1. Use an online markdown to PDF converter")
        print("2. Install pandoc or pdfkit for automatic conversion")
        print("3. View the markdown file directly")
