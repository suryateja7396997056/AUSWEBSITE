with open('HOME.HTML', 'r', encoding='utf-8') as f:
    content = f.read()

old_section = '''    <section class="bg-white py-24">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="font-display text-3xl md:text-5xl font-bold text-gray-900 mb-4">Our Complete <span class="text-brand-orange italic">Signage Arsenal</span></h2>
                <p class="text-gray-500 max-w-2xl mx-auto text-lg">A truly holistic approach to business branding. If it carries a message, we can print, cut, build, and install it.</p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="0">
                    <i class="fas fa-sticky-note text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Stickers & Labels</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Custom printed vinyl stickers and durable floor decals for both short-term campaigns and long-term branding.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="50">
                    <i class="fas fa-sign text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">A-Frame Signs</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Highly portable sandwich-boards perfect for grabbing sidewalk traffic, displaying daily specials, or directing customers.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="100">
                    <i class="fas fa-flag text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Banner Flags</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Dynamic outdoor feather and teardrop flags that catch the wind and customer attention effortlessly.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="150">
                    <i class="fas fa-th-large text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Corflute Signs</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Cost-effective, lightweight corrugated plastic signs ideal for real estate, construction sites, and event directions.</p>
                </div>
                
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="0">
                    <i class="fas fa-building text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Corporate Signage</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Specialty office wayfinding, directory boards, and building IDs tailored strictly to your corporate guidelines.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="50">
                    <i class="fas fa-utensils text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Marketing & Menu</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Sleek, easy-to-read menu boards and promotional displays customized for retail shops and hospitality venues.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="100">
                    <i class="fas fa-scroll text-2xl text-brand-orange mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Vinyl Banners</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Heavy-duty, weather-resistant vinyl and mesh roll-up banners engineered for tough outdoor events.</p>
                </div>
                <div class="p-6 rounded-2xl bg-gray-50 border border-gray-100 hover:shadow-lg transition-all card-lift" data-aos="zoom-in" data-aos-delay="150">
                    <i class="fas fa-window-maximize text-2xl text-brand-teal mb-4"></i>
                    <h4 class="font-bold text-gray-900 text-lg mb-2">Window Signs</h4>
                    <p class="text-sm text-gray-500 leading-relaxed">Frosted clings, custom window decals, and one-way vision graphics to utilize your glass space as a marketing tool.</p>
                </div>
            </div>
            
            <div class="flex justify-center mt-12">
                <div class="inline-flex items-center gap-3 bg-gray-900 text-white px-6 py-3 rounded-full text-sm font-bold">
                    <i class="fas fa-plus-circle text-brand-orange"></i> Plus Cut Vinyl Graphics & Premium Aluminium Composite Signs
                </div>
            </div>
        </div>
    </section>'''

new_section = '''    <section class="bg-white py-24">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="font-display text-3xl md:text-5xl font-bold text-gray-900 mb-4">Our Complete <span class="text-brand-orange italic">Signage Arsenal</span></h2>
                <p class="text-gray-500 max-w-2xl mx-auto text-lg">A truly holistic approach to business branding. If it carries a message, we can print, cut, build, and install it.</p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
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

if old_section in content:
    content = content.replace(old_section, new_section)
    with open('HOME.HTML', 'w', encoding='utf-8') as f:
        f.write(content)
    print('HOME.HTML services grid fixed successfully')
else:
    print('ERROR: Could not find old section in HOME.HTML')
