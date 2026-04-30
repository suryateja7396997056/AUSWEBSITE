import os
import re

# ========== index.html ==========
with open('index.html', 'r', encoding='utf-8') as f:
    home = f.read()

# 1. Remove LED Neon Signs from marquee
home = home.replace(' <span>★ LED Neon Signs</span>', '')

# 2. Add hero logo with TODO comment before the badge
hero_logo = '''                <!-- TODO: Replace with <img src="logo.png" alt="Budget Pro Solutions" class="h-8"> -->
                <a href="index.html" class="font-display font-bold text-3xl text-white mb-6 inline-block">BUDGET<span class="text-brand-orange">PRO</span></a>
                <div class="inline-flex items-center gap-2 bg-brand-orange/10 text-brand-orange px-4 py-2 rounded-full border border-brand-orange/20 font-mono text-xs font-bold tracking-widest uppercase mb-6 animate-float">'''
home = home.replace(
    '''                <div class="inline-flex items-center gap-2 bg-brand-orange/10 text-brand-orange px-4 py-2 rounded-full border border-brand-orange/20 font-mono text-xs font-bold tracking-widest uppercase mb-6 animate-float">''',
    hero_logo
)

# 3. Replace 3rd flagship card (LED Neon) with Cut Vinyl Graphics
old_flagship = '''                <div class="bg-brand-dark rounded-3xl p-8 shadow-xl border border-white/10 card-lift relative overflow-hidden" data-aos="fade-up" data-aos-delay="200">
                    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-orange-500/20 via-transparent to-transparent"></div>
                    <div class="img-reveal mb-8 h-60">
                        <img src="https://images.unsplash.com/photo-1563298723-dcfebaa392e3?w=600&q=80" alt="LED Neon Signage" class="w-full h-full object-cover">
                    </div>
                    <div class="flex items-center gap-3 mb-4 relative z-10">
                        <i class="fas fa-bolt text-brand-yellow text-xl"></i>
                        <h3 class="font-display text-2xl font-bold text-white">LED Neon Signage</h3>
                    </div>
                    <p class="text-white/70 text-sm leading-relaxed mb-6 relative z-10">
                        Stand out in the dark with modern, energy-efficient LED signage. From custom neon-style lettering for cafes to illuminated 3D logos for corporate facades, we bring your brand to life with stunning luminescence.
                    </p>
                    <a href="https://wa.me/64450946690?text=I%20need%20details%20on%20LED%20Neon%20Signage" class="inline-flex items-center gap-2 text-brand-yellow font-bold text-sm tracking-wide group hover:underline relative z-10">
                        Explore Service <i class="fas fa-arrow-right transform group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>'''

new_flagship = '''                <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-100 card-lift" data-aos="fade-up" data-aos-delay="200">
                    <div class="img-reveal mb-8 h-60">
                        <img src="https://images.unsplash.com/photo-161-B8A3D9F6D9B8?w=600&q=80" alt="Cut Vinyl Graphics" class="w-full h-full object-cover">
                    </div>
                    <div class="flex items-center gap-3 mb-4">
                        <i class="fas fa-cut text-brand-teal text-xl"></i>
                        <h3 class="font-display text-2xl font-bold text-gray-900">Cut Vinyl Graphics</h3>
                    </div>
                    <p class="text-gray-600 text-sm leading-relaxed mb-6">
                        Precision-cut vinyl lettering and decals for vehicles, windows, walls, and floors. We use premium cast vinyl for crisp edges and long-term adhesion that withstands harsh AU/NZ conditions.
                    </p>
                    <a href="cut-vinyl-graphics.html" class="inline-flex items-center gap-2 text-brand-teal font-bold text-sm tracking-wide group hover:underline">
                        Explore Service <i class="fas fa-arrow-right transform group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>'''
home = home.replace(old_flagship, new_flagship)

# 4. Replace services grid with 3x4 layout showing all 12 services
old_grid_start = home.find('<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">')
old_grid_end = home.find('</section>\n    <section class="section-dark py-24 relative overflow-hidden">')

new_services_grid = '''            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="0">
                    <i class="fas fa-print text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Large Format Printing</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Breathtaking visual clarity on a massive scale — pop-up displays, event banners, and exhibition boards.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="50">
                    <i class="fas fa-car text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Vehicle Signage</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Full wraps, partial wraps, and precision-cut vinyl decals that turn fleets into mobile billboards.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="100">
                    <i class="fas fa-building text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Corporate Signage</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Office wayfinding, directory boards, and building IDs tailored to your corporate guidelines.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="150">
                    <i class="fas fa-window-maximize text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Window Signs</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Frosted clings, custom decals, and one-way vision graphics to utilize glass as a marketing tool.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="0">
                    <i class="fas fa-scroll text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Vinyl & Mesh Banners</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Heavy-duty, weather-resistant vinyl and mesh roll-up banners engineered for tough outdoor events.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="50">
                    <i class="fas fa-cut text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Cut Vinyl Graphics</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Precision-cut lettering and decals for vehicles, windows, walls, and floors using premium cast vinyl.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="100">
                    <i class="fas fa-flag text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Banner Flags</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Dynamic outdoor feather and teardrop flags that catch the wind and customer attention effortlessly.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="150">
                    <i class="fas fa-sign text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">A-Frame Signs</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Highly portable sandwich-boards perfect for grabbing sidewalk traffic and displaying daily specials.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="0">
                    <i class="fas fa-th-large text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Corflute Signs</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Cost-effective, lightweight corrugated plastic signs ideal for real estate, construction, and events.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="50">
                    <i class="fas fa-layer-group text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Aluminium Signs</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Premium aluminium composite panel signs for architectural fascias and long-term outdoor branding.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="100">
                    <i class="fas fa-utensils text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Marketing & Menu</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Sleek, easy-to-read menu boards and promotional displays for retail shops and hospitality venues.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="150">
                    <i class="fas fa-sticky-note text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Stickers & Labels</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Custom printed vinyl stickers and durable floor decals for short-term campaigns and long-term branding.</p>
                </div>
            </div>
            
        </div>
    </section>'''

if old_grid_start != -1 and old_grid_end != -1:
    home = home[:old_grid_start] + new_services_grid + home[old_grid_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home)
print('Updated index.html')

# ========== our-portfolio.html ==========
with open('our-portfolio.html', 'r', encoding='utf-8') as f:
    port = f.read()

old_gallery = '''                <div class="img-reveal rounded-3xl shadow-md" data-aos="zoom-in" data-aos-delay="100">
                    <img src="https://images.unsplash.com/photo-1563298723-dcfebaa392e3?w=800&q=80" alt="LED Neon Sign" />
                    <div class="img-overlay">
                        <h4 class="text-white font-bold text-xl mb-1">Custom LED Neon</h4>
                        <p class="text-brand-orange font-mono text-xs uppercase tracking-widest">Illuminated Signage</p>
                    </div>
                </div>'''

new_gallery = '''                <div class="img-reveal rounded-3xl shadow-md" data-aos="zoom-in" data-aos-delay="100">
                    <img src="https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&q=80" alt="Vehicle Fleet Wrap" />
                    <div class="img-overlay">
                        <h4 class="text-white font-bold text-xl mb-1">Vehicle Fleet Wrap</h4>
                        <p class="text-brand-orange font-mono text-xs uppercase tracking-widest">Vehicle Signage</p>
                    </div>
                </div>'''

port = port.replace(old_gallery, new_gallery)

with open('our-portfolio.html', 'w', encoding='utf-8') as f:
    f.write(port)
print('Updated our-portfolio.html')

# ========== contact-us.html ==========
with open('contact-us.html', 'r', encoding='utf-8') as f:
    contact = f.read()

# Change grid from 3 to 4 columns and add address card
old_contact_grid = '''    <section class="relative -mt-20 z-20 pb-20">
        <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-6">
            <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100 card-lift text-center" data-aos="fade-up" data-aos-delay="0">
                <div class="w-16 h-16 bg-brand-teal/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
                    <i class="fas fa-phone-alt text-2xl text-brand-teal"></i>
                </div>
                <h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Call Us Directly</h3>
                <p class="text-gray-500 text-sm mb-6">Speak with our signage experts instantly during business hours.</p>
                <a href="tel:+64450946690" class="text-brand-teal font-bold text-lg hover:underline">+64 450946690</a>
            </div>

            <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100 card-lift text-center" data-aos="fade-up" data-aos-delay="100">
                <div class="w-16 h-16 bg-brand-orange/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
                    <i class="fas fa-envelope text-2xl text-brand-orange"></i>
                </div>
                <h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Send an Email</h3>
                <p class="text-gray-500 text-sm mb-6">Send your artwork files, dimensions, and project details.</p>
                <a href="mailto:enquiry@budgetprosolutions.com.au" class="text-brand-orange font-bold text-base hover:underline break-all">enquiry@budgetprosolutions.com.au</a>
            </div>

            <div class="bg-brand-dark rounded-3xl p-8 shadow-xl border border-white/10 card-lift text-center relative overflow-hidden" data-aos="fade-up" data-aos-delay="200">
                <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_right,_var(--tw-gradient-stops))] from-green-500/20 via-transparent to-transparent"></div>
                <div class="relative z-10">
                    <div class="w-16 h-16 bg-green-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
                        <i class="fab fa-whatsapp text-2xl text-green-400"></i>
                    </div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2">WhatsApp Chat</h3>
                    <p class="text-white/60 text-sm mb-6">The fastest way to get a quote. Send us photos of your site instantly.</p>
                    <a href="https://wa.me/64450946690?text=Hi%20Budget%20Pro,%20I%20would%20like%20to%20request%20a%20quote." class="inline-block bg-[#25D366] text-white px-6 py-2 rounded-full font-bold shadow-lg hover:scale-105 transition-transform">Chat Now</a>
                </div>
            </div>
        </div>
    </section>'''

new_contact_grid = '''    <section class="relative -mt-20 z-20 pb-20">
        <div class="max-w-7xl mx-auto px-6 grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100 card-lift text-center" data-aos="fade-up" data-aos-delay="0">
                <div class="w-16 h-16 bg-brand-teal/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
                    <i class="fas fa-phone-alt text-2xl text-brand-teal"></i>
                </div>
                <h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Call Us Directly</h3>
                <p class="text-gray-500 text-sm mb-6">Speak with our signage experts instantly during business hours.</p>
                <a href="tel:+64450946690" class="text-brand-teal font-bold text-lg hover:underline">+64 450946690</a>
            </div>

            <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100 card-lift text-center" data-aos="fade-up" data-aos-delay="100">
                <div class="w-16 h-16 bg-brand-orange/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
                    <i class="fas fa-envelope text-2xl text-brand-orange"></i>
                </div>
                <h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Send an Email</h3>
                <p class="text-gray-500 text-sm mb-6">Send your artwork files, dimensions, and project details.</p>
                <a href="mailto:enquiry@budgetprosolutions.com.au" class="text-brand-orange font-bold text-base hover:underline break-all">enquiry@budgetprosolutions.com.au</a>
            </div>

            <div class="bg-brand-dark rounded-3xl p-8 shadow-xl border border-white/10 card-lift text-center relative overflow-hidden" data-aos="fade-up" data-aos-delay="200">
                <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_right,_var(--tw-gradient-stops))] from-green-500/20 via-transparent to-transparent"></div>
                <div class="relative z-10">
                    <div class="w-16 h-16 bg-green-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
                        <i class="fab fa-whatsapp text-2xl text-green-400"></i>
                    </div>
                    <h3 class="font-display text-2xl font-bold text-white mb-2">WhatsApp Chat</h3>
                    <p class="text-white/60 text-sm mb-6">The fastest way to get a quote. Send us photos of your site instantly.</p>
                    <a href="https://wa.me/64450946690?text=Hi%20Budget%20Pro,%20I%20would%20like%20to%20request%20a%20quote." class="inline-block bg-[#25D366] text-white px-6 py-2 rounded-full font-bold shadow-lg hover:scale-105 transition-transform">Chat Now</a>
                </div>
            </div>

            <div class="bg-white rounded-3xl p-8 shadow-xl border border-gray-100 card-lift text-center" data-aos="fade-up" data-aos-delay="300">
                <div class="w-16 h-16 bg-brand-yellow/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
                    <i class="fas fa-map-marker-alt text-2xl text-brand-yellow"></i>
                </div>
                <h3 class="font-display text-2xl font-bold text-gray-900 mb-2">Visit Our Workshop</h3>
                <p class="text-gray-500 text-sm mb-6">Drop by to discuss your project in person or collect your order.</p>
                <span class="text-brand-yellow font-bold text-sm">Unit 2, 7 Basalt Street,<br>Geebung, QLD 4034</span>
            </div>
        </div>
    </section>'''

contact = contact.replace(old_contact_grid, new_contact_grid)

with open('contact-us.html', 'w', encoding='utf-8') as f:
    f.write(contact)
print('Updated contact-us.html')

print('Special changes done.')
