document.addEventListener('DOMContentLoaded', function() {
    // Load brands when page loads
    loadBrands();
    
    // Add event listeners
    document.getElementById('brand').addEventListener('change', loadModels);
    document.getElementById('searchForm').addEventListener('submit', performSearch);
});

async function loadBrands() {
    try {
        const response = await fetch('/api/brands');
        const brands = await response.json();
        const brandSelect = document.getElementById('brand');
        
        brands.forEach(brand => {
            const option = document.createElement('option');
            option.value = brand.id;
            option.textContent = brand.name;
            brandSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading brands:', error);
    }
}

async function loadModels() {
    const brandId = document.getElementById('brand').value;
    if (!brandId) return;
    
    try {
        const response = await fetch(`/api/models/${brandId}`);
        const models = await response.json();
        const modelSelect = document.getElementById('model');
        
        // Clear existing options
        modelSelect.innerHTML = '<option value="">Izaberite model</option>';
        
        models.forEach(model => {
            const option = document.createElement('option');
            option.value = model.id;
            option.textContent = `${model.name} (${model.year_start}-${model.year_end})`;
            modelSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading models:', error);
    }
}

async function performSearch(event) {
    event.preventDefault();
    
    const params = new URLSearchParams({
        brand_id: document.getElementById('brand').value,
        model_id: document.getElementById('model').value,
        engine_type: document.getElementById('engineType').value,
        min_power: document.getElementById('minPower').value,
        max_power: document.getElementById('maxPower').value
    });
    
    try {
        const response = await fetch(`/api/search?${params}`);
        const results = await response.json();
        displayResults(results);
    } catch (error) {
        console.error('Error performing search:', error);
    }
}

function displayResults(results) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';
    
    if (results.length === 0) {
        resultsContainer.innerHTML = '<div class="col-12"><div class="alert alert-info">Nema pronađenih rezultata</div></div>';
        return;
    }
    
    results.forEach(result => {
        const card = document.createElement('div');
        card.className = 'col-md-6 col-lg-4 mb-4';
        card.innerHTML = `
            <div class="car-card h-100" style="cursor: pointer" onclick="window.location.href='/model/${result.model.id}'">
                <div class="car-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                        <path d="M499.99 176h-59.87l-16.64-41.6C406.38 91.63 365.57 64 319.5 64h-127c-46.06 0-86.88 27.63-103.99 70.4L71.87 176H12.01C4.2 176-1.53 183.34.37 190.91l6 24C7.7 220.25 12.5 224 18.01 224h20.07C24.65 235.73 16 252.78 16 272v48c0 16.12 6.16 30.67 16 41.93V416c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32v-32h256v32c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32v-54.07c9.84-11.25 16-25.8 16-41.93v-48c0-19.22-8.65-36.27-22.07-48H494c5.51 0 10.31-3.75 11.64-9.09l6-24c1.89-7.57-3.84-14.91-11.65-14.91zm-352.06-17.83c7.29-18.22 24.94-30.17 44.57-30.17h127c19.63 0 37.28 11.95 44.57 30.17L384 208H128l19.93-49.83zM96 319.8c-19.2 0-32-12.76-32-31.9S76.8 256 96 256s48 28.71 48 47.85-28.8 15.95-48 15.95zm320 0c-19.2 0-48 3.19-48-15.95S396.8 256 416 256s32 12.76 32 31.9-12.8 31.9-32 31.9z"/>
                    </svg>
                </div>
                <div class="car-content">
                    <div class="car-header">
                        <h5 class="car-title">${result.model.name}</h5>
                        <div class="car-years">
                            <svg class="year-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                                <path d="M152 24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H64C28.7 64 0 92.7 0 128v16 48V448c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V192 144 128c0-35.3-28.7-64-64-64H344V24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H152V24zM48 192h352V448c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V192z"/>
                            </svg>
                            <span>${result.model.year_start} - ${result.model.year_end}</span>
                        </div>
                    </div>
                    
                    <div class="specs-section">
                        <div class="engine-type">
                            <span class="engine-badge ${result.engine.type}">
                                ${result.engine.type.toUpperCase()}
                            </span>
                        </div>
                        
                        <div class="specs-grid">
                            <div class="spec-item">
                                <div class="spec-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                        <path d="M7 4v2h3v2H7l-2 2v3H3v-3H1v8h2v-3h2v3h3l2 2h8v-4h2v3h3V9h-3v3h-2V8h-6V6h3V4H7zm9 9h5v6h-1v-3h-2v3h-1v-3h-2v3h-1v-2h2v-4z"/>
                                    </svg>
                                </div>
                                <div class="spec-details">
                                    <span class="spec-label">Zapremina</span>
                                    <span class="spec-value">${result.engine.displacement}L</span>
                                </div>
                            </div>
                            
                            <div class="spec-item">
                                <div class="spec-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                        <path d="M12 16c1.66 0 3-1.34 3-3 0-1.31-1.16-2.94-3-4.5-1.84 1.56-3 3.19-3 4.5 0 1.66 1.34 3 3 3zm0-12c4.97 0 9 4.03 9 9s-4.03 9-9 9-9-4.03-9-9 4.03-9 9-9zm0 16c3.86 0 7-3.14 7-7s-3.14-7-7-7-7 3.14-7 7 3.14 7 7 7z"/>
                                    </svg>
                                </div>
                                <div class="spec-details">
                                    <span class="spec-label">Snaga</span>
                                    <span class="spec-value">${result.engine.power} KS</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        resultsContainer.appendChild(card);
    });
}
