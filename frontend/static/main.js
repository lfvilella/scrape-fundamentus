var app = new Vue({
  el: '#app',
  data: {
    assetsList: [],
    errors: { 'aaa': 'Ativo não encontrado.', 'bbb': 'Ativo não encontrado.' },
    search: '',
    isLoading: false,
    showAssets: false,
    showErros: false,
  },
  methods: {
    cleanErrors: function () {
      this.errors = {};
      this.showErros = false;
    },
    getFormattedParam: function (search) {
      let _search = search.replace(/\s/g, '');
      _search = _search.split(',');
      return _search;
    },
    getAssets: function (search) {
      this.showAssets = false;
      this.isLoading = true;
      const params = {
        assets: this.getFormattedParam(search),
      }
      axios.post('/api/v.1/scraper', params, { timeout: 300000 })  // 5 minutes
        .then((response) => {
          this.assetsList = response.data.results.map(
            row => ({
              div_yield: row.div_yield,
              ebitda: row.ebitda || '---',
              max_price: row.max_price,
              min_price: row.min_price,
              p_l: row.p_l || '---',
              p_vp: row.p_vp,
              price: row.price,
              roe: row.roe || '---',
              roic: row.roic || '---',
              subsector_or_segment: row.subsector_or_segment,
              ticket: row.ticket,
            })
          );

          if (Object.keys(response.data.errors).length !== 0) {
            this.errors = response.data.errors;
            this.showErros = true;
          }

          this.isLoading = false;
          this.showAssets = true;
        })
        .catch((error) => {
          this.assetsList = [];
          this.errors = {};
          this.isLoading = false;
          console.log(error)
        });
    },
  }
})
