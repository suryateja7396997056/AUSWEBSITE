import os
import re

# Meta descriptions mapped by filename
META_DESC = {
    'HOME.HTML': 'Budget Pro Solutions delivers premium signage, vehicle wraps, banners, and corporate branding across Australia and New Zealand.',
    'About Us.HTML': 'Learn about Budget Pro Solutions — AU/NZ\'s trusted signage partner for large-format printing, vehicle wraps, and corporate branding.',
    'Contact Us.HTML': 'Get a free quote for custom signage. Contact Budget Pro Solutions via WhatsApp, phone, or email.',
    'Our Portfolio.HTML': 'Explore our portfolio of professional signage projects including vehicle wraps, corporate signage, banners, and more across Australia and New Zealand.',
    'Large Format Printing.HTML': 'Premium large format printing services for banners, exhibitions, and retail displays across Australia and New Zealand.',
    'Vehicle Signage.HTML': 'Custom vehicle wraps, fleet branding, and vinyl lettering that turn your cars into mobile billboards across AU/NZ.',
    'Corporate Signage.HTML': 'Executive corporate signage, 3D reception logos, wayfinding, and office fit-outs across Australia and New Zealand.',
    'Window Signs.HTML': 'Custom window signs, frosted privacy films, and one-way vision graphics for retail and corporate spaces across AU/NZ.',
    'Vinyl & Mesh Banners.HTML': 'Heavy-duty vinyl and wind-permeable mesh banners for events, construction sites, and outdoor advertising across AU/NZ.',
    'Cut Vinyl Graphics.HTML': 'Precision cut vinyl lettering, vehicle decals, window lettering, and die-cut logos across Australia and New Zealand.',
    'Banner Flags.HTML': 'Dynamic outdoor feather and teardrop banner flags designed to catch attention at events and storefronts across AU/NZ.',
    'A-Frame Signs.HTML': 'Portable A-frame sandwich boards perfect for sidewalk advertising, daily specials, and directional signage across AU/NZ.',
    'Corflute Signs.HTML': 'Cost-effective corflute signs for real estate, construction, and events across Australia and New Zealand.',
    'Aluminium Signs.HTML': 'Premium aluminium composite panel signs for architectural fascias, building IDs, and long-term outdoor branding across AU/NZ.',
    'Marketing & Menu Signs.HTML': 'Sleek menu boards, promotional displays, and marketing signage tailored for retail and hospitality across AU/NZ.',
    'Stickers & Labels.HTML': 'Custom vinyl stickers, product labels, floor decals, and die-cut decals for businesses across Australia and New Zealand.',
}

HEADER_HTML = '''<header class="sticky top-0 z-50 bg-brand-dark/95 backdrop-blur border-b border-white/10">
    <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        <a href="HOME.HTML" class="font-display font-bold text-2xl text-white">BUDGET<span class="text-brand-orange">PRO</span></a>
        <nav class="hidden md:flex items-center gap-8 text-sm font-medium text-white/80">
            <a href="HOME.HTML" class="hover:text-white transition-colors">Home</a>
            <div class="relative group">
                <button class="flex items-center gap-1 hover:text-white transition-colors">Services <i class="fas fa-chevron-down text-xs"></i></button>
                <div class="absolute top-full left-0 mt-2 w-56 bg-brand-dark border border-white/10 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 p-2">
                    <a href="Large Format Printing.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Large Format Printing</a>
                    <a href="Vehicle Signage.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Vehicle Signage & Wraps</a>
                    <a href="Corporate Signage.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Corporate Signage</a>
                    <a href="Window Signs.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Window Signs & Graphics</a>
                    <a href="Vinyl & Mesh Banners.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Vinyl & Mesh Banners</a>
                    <a href="Cut Vinyl Graphics.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Cut Vinyl Graphics</a>
                    <a href="Banner Flags.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Banner Flags</a>
                    <a href="A-Frame Signs.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">A-Frame Signs</a>
                    <a href="Corflute Signs.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Corflute Signs</a>
                    <a href="Aluminium Signs.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Aluminium Signs</a>
                    <a href="Marketing & Menu Signs.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Marketing & Menu Signs</a>
                    <a href="Stickers & Labels.HTML" class="block px-4 py-2 rounded-lg hover:bg-white/10 text-white/80 hover:text-white text-sm">Stickers & Labels</a>
                </div>
            </div>
            <a href="Our Portfolio.HTML" class="hover:text-white transition-colors">Portfolio</a>
            <a href="About Us.HTML" class="hover:text-white transition-colors">About</a>
            <a href="Contact Us.HTML" class="hover:text-white transition-colors">Contact</a>
        </nav>
        <a href="Contact Us.HTML" class="hidden md:inline-flex bg-brand-orange hover:bg-orange-600 text-white px-6 py-2.5 rounded-full text-sm font-bold transition-all">Get Quote</a>
        <button id="mobile-menu-btn" class="md:hidden text-white text-2xl"><i class="fas fa-bars"></i></button>
    </div>
    <div id="mobile-menu" class="md:hidden hidden bg-brand-dark border-t border-white/10 px-6 py-4">
        <nav class="flex flex-col gap-3 text-sm font-medium text-white/80">
            <a href="HOME.HTML" class="hover:text-white transition-colors">Home</a>
            <span class="text-white/40 text-xs uppercase tracking-wider font-bold mt-2">Services</span>
            <a href="Large Format Printing.HTML" class="pl-2 hover:text-white transition-colors">Large Format Printing</a>
            <a href="Vehicle Signage.HTML" class="pl-2 hover:text-white transition-colors">Vehicle Signage & Wraps</a>
            <a href="Corporate Signage.HTML" class="pl-2 hover:text-white transition-colors">Corporate Signage</a>
            <a href="Window Signs.HTML" class="pl-2 hover:text-white transition-colors">Window Signs & Graphics</a>
            <a href="Vinyl & Mesh Banners.HTML" class="pl-2 hover:text-white transition-colors">Vinyl & Mesh Banners</a>
            <a href="Cut Vinyl Graphics.HTML" class="pl-2 hover:text-white transition-colors">Cut Vinyl Graphics</a>
            <a href="Banner Flags.HTML" class="pl-2 hover:text-white transition-colors">Banner Flags</a>
            <a href="A-Frame Signs.HTML" class="pl-2 hover:text-white transition-colors">A-Frame Signs</a>
            <a href="Corflute Signs.HTML" class="pl-2 hover:text-white transition-colors">Corflute Signs</a>
            <a href="Aluminium Signs.HTML" class="pl-2 hover:text-white transition-colors">Aluminium Signs</a>
            <a href="Marketing & Menu Signs.HTML" class="pl-2 hover:text-white transition-colors">Marketing & Menu Signs</a>
            <a href="Stickers & Labels.HTML" class="pl-2 hover:text-white transition-colors">Stickers & Labels</a>
            <a href="Our Portfolio.HTML" class="hover:text-white transition-colors mt-2">Portfolio</a>
            <a href="About Us.HTML" class="hover:text-white transition-colors">About</a>
            <a href="Contact Us.HTML" class="hover:text-white transition-colors">Contact</a>
            <a href="Contact Us.HTML" class="bg-brand-orange text-white px-6 py-2.5 rounded-full text-sm font-bold text-center mt-2">Get Quote</a>
        </nav>
    </div>
</header>
<script>
    document.getElementById('mobile-menu-btn').addEventListener('click', () => {
        document.getElementById('mobile-menu').classList.toggle('hidden');
    });
</script>
'''

FOOTER_HTML = '''    <footer class="bg-brand-dark pt-20 pb-8 border-t border-white/5">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid md:grid-cols-3 gap-12 mb-16">
                <div>
                    <!-- TODO: Replace with <img src="logo.png" alt="Budget Pro Solutions" class="h-8"> -->
                    <a href="HOME.HTML" class="font-display font-bold text-3xl text-white mb-6 inline-block">BUDGET<span class="text-brand-orange">PRO</span></a>
                    <p class="text-white/40 text-sm leading-relaxed mb-6">
                        Specializing in the production, installation, and management of general signage and high-quality visual solutions across AU/NZ to boost brand exposure.
                    </p>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-6 tracking-wide">Solutions</h4>
                    <ul class="space-y-3 text-white/40 text-sm">
                        <li><a href="Large Format Printing.HTML" class="hover:text-white transition-colors">Large Format Printing</a></li>
                        <li><a href="Vehicle Signage.HTML" class="hover:text-white transition-colors">Vehicle Signage & Wraps</a></li>
                        <li><a href="Corporate Signage.HTML" class="hover:text-white transition-colors">Corporate Signage</a></li>
                        <li><a href="Window Signs.HTML" class="hover:text-white transition-colors">Window Signs & Graphics</a></li>
                        <li><a href="Vinyl & Mesh Banners.HTML" class="hover:text-white transition-colors">Vinyl & Mesh Banners</a></li>
                        <li><a href="Cut Vinyl Graphics.HTML" class="hover:text-white transition-colors">Cut Vinyl Graphics</a></li>
                        <li><a href="Banner Flags.HTML" class="hover:text-white transition-colors">Banner Flags</a></li>
                        <li><a href="A-Frame Signs.HTML" class="hover:text-white transition-colors">A-Frame Signs</a></li>
                        <li><a href="Corflute Signs.HTML" class="hover:text-white transition-colors">Corflute Signs</a></li>
                        <li><a href="Aluminium Signs.HTML" class="hover:text-white transition-colors">Aluminium Signs</a></li>
                        <li><a href="Marketing & Menu Signs.HTML" class="hover:text-white transition-colors">Marketing & Menu Signs</a></li>
                        <li><a href="Stickers & Labels.HTML" class="hover:text-white transition-colors">Stickers & Labels</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-bold mb-6 tracking-wide">Get In Touch</h4>
                    <ul class="space-y-4 text-white/60 text-sm">
                        <li class="flex items-center gap-3">
                            <i class="fas fa-envelope text-brand-orange w-4"></i>
                            <a href="mailto:enquiry@budgetprosolutions.com.au" class="hover:text-white transition-colors">enquiry@budgetprosolutions.com.au</a>
                        </li>
                        <li class="flex items-center gap-3">
                            <i class="fas fa-phone text-brand-orange w-4"></i>
                            <a href="tel:+64450946690" class="hover:text-white transition-colors">+64 450946690</a>
                        </li>
                        <li class="flex items-start gap-3">
                            <i class="fas fa-map-marker-alt text-brand-orange w-4 mt-0.5"></i>
                            <span>Unit 2, 7 Basalt Street, Geebung, QLD 4034</span>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-white/10 pt-8 text-center flex flex-col md:flex-row items-center justify-between gap-4">
                <p class="text-white/30 text-xs font-mono uppercase tracking-widest">&copy; 2026 Budget Pro Solutions. All Rights Reserved.</p>
                <div class="flex gap-4 text-white/40">
                    <a href="#" aria-label="Facebook" class="hover:text-white transition-colors"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" aria-label="Instagram" class="hover:text-white transition-colors"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
    </footer>'''

files = [f for f in os.listdir('.') if f.endswith('.HTML')]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Add meta description after </title> if missing
    desc = META_DESC.get(fname, '')
    if desc and '<meta name="description"' not in content:
        content = content.replace('</title>', f'</title>\n    <meta name="description" content="{desc}" />')
    
    # 2. Add scroll-padding-top to CSS
    if 'scroll-padding-top' not in content:
        content = content.replace(
            'body { font-family: \'Outfit\', sans-serif;',
            'html { scroll-padding-top: 80px; }\n        body { font-family: \'Outfit\', sans-serif;'
        )
    
    # 3. Insert header after body tag
    if '<header class="sticky top-0' not in content:
        content = content.replace(
            '<body class="noise-overlay text-gray-800">\n',
            '<body class="noise-overlay text-gray-800">\n\n' + HEADER_HTML
        )
    
    # 4. Replace footer block
    footer_start = content.find('<footer class="bg-brand-dark pt-20 pb-8 border-t border-white/5">')
    footer_end = content.find('</footer>')
    if footer_start != -1 and footer_end != -1:
        footer_end += len('</footer>')
        content = content[:footer_start] + FOOTER_HTML + content[footer_end:]
    
    if content != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {fname}')
    else:
        print(f'No changes: {fname}')

print('Done with standard changes.')
