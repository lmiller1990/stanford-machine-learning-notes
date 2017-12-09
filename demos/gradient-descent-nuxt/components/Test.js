export default {
  data () {
    return {
      val: 0,
      vals: [1, 2, 3]
    }
  },

  created () {
    setInterval(() => {
      this.val += 1
    }, 500)
  },

  computed: {
    time () {
      return this.val
    }
  },

  render () {
    return (
      <div>Hi. The time is: {this.time}. Here are some vals: {this.vals.map(x => <div key={x}>{x}</div>)}</div>
    )
  }
}
