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
        card.className = 'col-md-6 col-lg-4';
        card.innerHTML = `
            <div class="card result-card h-100" style="cursor: pointer" onclick="window.location.href='/model/${result.model.id}'">
                <div class="card-body">
                    <h5 class="card-title">${result.model.name}</h5>
                    <p class="card-text">
                        <small class="text-muted">${result.model.year_start} - ${result.model.year_end}</small>
                    </p>
                    <div class="mb-2">
                        <span class="engine-badge ${result.engine.type}">
                            ${result.engine.type}
                        </span>
                    </div>
                    <p class="card-text">
                        <strong>Zapremina:</strong> ${result.engine.displacement}L<br>
                        <strong>Snaga:</strong> ${result.engine.power} KS
                    </p>
                </div>
            </div>
        `;
        resultsContainer.appendChild(card);
    });
}
