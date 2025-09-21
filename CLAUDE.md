# peerpressure Website - Maintenance Guide

## Website Purpose

Static website hosting the **privacy policy** and landing page for **peerpressure.social**. This site is critical for Google Play Store compliance as it hosts the required privacy policy at `/privacy`.

## Site Architecture

- **Hosting**: GitHub Pages
- **Domain**: peerpressure.social (configured via CNAME)
- **Structure**: Static HTML with minimal styling
- **Repository**: https://github.com/axolotl-systems/peerpressure-landing

## Key Files

### **Critical Files (Do Not Modify Carelessly)**
- **`CNAME`**: Domain configuration for GitHub Pages (contains "peerpressure.social")
- **`privacy/index.html`**: Privacy policy required by Google Play Store
- **`index.html`**: Main landing page

### **Supporting Files**
- **`README.md`**: Basic website documentation
- **Screenshots and assets**: Supporting visual content for the landing page

## Privacy Policy Management

### **Current Status**
- **URL**: https://peerpressure.social/privacy
- **Status**: ✅ **Live and Compliant**
- **Google Play Requirement**: ✅ **Satisfied**
- **Template Source**: Based on `/peerpressure_app/PRIVACY_POLICY.md`

### **Update Procedure**
When privacy policy needs updates:

1. **Edit Template**: Update `/peerpressure_app/PRIVACY_POLICY.md` first
2. **Update Website**: Modify `privacy/index.html` with same content
3. **Commit Changes**: Push to GitHub for automatic deployment
4. **Verify Live**: Check https://peerpressure.social/privacy (2-3 min delay)
5. **Update Documentation**: Note changes in `/peerpressure_app/PRIVACY_COMPLIANCE.md`

### **Critical Requirements**
- **Public Accessibility**: Must remain publicly accessible at all times
- **Google Play Compliance**: Required for app store approval
- **Content Accuracy**: Must match actual app data collection practices
- **Contact Information**: Must include valid contact email (privacy@peerpressure.social)

## Development Workflow

### **Making Updates**
```bash
# Navigate to website directory
cd /Users/anneschuth/peerpressure/peerpressure-landing

# Edit files as needed
# Commit and push changes
git add .
git commit -m "Update website content"
git push

# Verify deployment (GitHub Pages auto-deploys)
# Check https://peerpressure.social after 2-3 minutes
```

### **Testing Changes**
- **Local Testing**: Open HTML files directly in browser
- **Live Verification**: Always verify changes are live at peerpressure.social
- **Mobile Testing**: Ensure privacy policy is readable on mobile devices

## Domain Configuration

### **GitHub Pages Setup**
- **Source**: Deploy from main branch
- **Custom Domain**: peerpressure.social (configured via CNAME file)
- **HTTPS**: Enabled automatically by GitHub Pages
- **DNS**: Configured externally to point to GitHub Pages

### **Important Notes**
- **CNAME File**: Never delete or modify unless changing domains
- **DNS Propagation**: Changes may take time to propagate globally
- **Certificate**: GitHub automatically manages SSL certificate

## Maintenance Tasks

### **Regular Checks**
- **Monthly**: Verify privacy policy is accessible
- **After App Updates**: Check if privacy policy needs updates
- **Google Play Releases**: Ensure privacy policy URL works in store listing

### **Emergency Procedures**
If privacy policy becomes inaccessible:
1. **Check GitHub Pages Status**: Verify deployment is working
2. **Check Domain DNS**: Ensure peerpressure.social points to GitHub
3. **Backup Option**: Temporarily host policy elsewhere if needed
4. **Update Google Play**: Change privacy policy URL if domain changes

## Content Guidelines

### **Privacy Policy Content**
- **Camera Permission**: Must explain QR code scanning usage
- **Firebase Data**: Must document data collection and storage
- **User Rights**: Must include access, deletion, and portability rights
- **Contact Info**: Must provide valid contact email

### **Landing Page Content**
- **App Description**: Brief overview of peerpressure app
- **Download Links**: Links to app stores (when available)
- **Privacy Link**: Clear link to privacy policy
- **Contact Information**: Support and privacy contact details

## Integration with App Development

### **Relationship to App**
- **Privacy Policy**: Required for Google Play Store app approval
- **URL Reference**: App documentation references https://peerpressure.social/privacy
- **Compliance**: Website must stay live for app to remain in stores

### **Coordination Requirements**
- **App Feature Changes**: May require privacy policy updates
- **Data Collection Changes**: Must update privacy policy immediately
- **Store Submissions**: Verify privacy policy is accessible before submission

---

**Website Status**: ✅ Live and fully functional
**Last Updated**: September 2024
**Critical Dependency**: Required for Google Play Store compliance