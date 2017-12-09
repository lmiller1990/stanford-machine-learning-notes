export default {
  name: 'Graph',

  props: {
    points: {
      type: Array,
      required: true
    }
  },

  created () {
    this.points.map(val =>
      console.log(val['x'] * 50, val['y'] / 10)
    )
  },
  render () {
    return (
      <svg style="border: 1px solid black" stroke="#000" stroke-width="1" width="650" height="650">
        {this.points.map(val =>
          <circle cx={val['x'] * 50} cy={val['y'] / -10} stroke="#FF0000" fill="#FFF" stroke-width="3" r="5"/>
        )}
      </svg>
    )
  }
}
