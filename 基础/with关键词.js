const mockWindow = {
  document: {
    querySelector: (selector) => {
      console.log('From Mock Window:', selector)
    }
  }
}

with(mockWindow) {
  document.querySelector('#app')
  eval("document.querySelector('#app')")
}