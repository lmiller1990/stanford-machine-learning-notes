import Features from './Features'
import Graph from './Graph'

export default {
  components: {
    Features,
    Graph
  },

  data () {
    return {
      ALPHA: 0.0005,
      x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      y: [-890, -1411, -1560, -2220, -2091, -2878, -3537, -3268, -3920, -4163, -5471, -5157],
      points: []
    }
  },

  created () {
    for (let i = 0; i < this.x.length; i++) {
      this.points.push({ x: this.x[i], y: this.y[i] })
    }
  },

  render () {
    return (
      <div>
        <Features x={this.x} y={this.y} />
        <Graph learningRate={this.ALPHA} points={this.points} />
      </div>
    )
  }
}
