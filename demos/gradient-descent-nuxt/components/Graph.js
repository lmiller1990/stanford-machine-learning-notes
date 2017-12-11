export default {
  name: 'Graph',

  props: {
    learningRate: {
      type: Number,
      required: true
    },

    points: {
      type: Array,
      required: true
    }
  },

  data () {
    return {
      thetaZero: 0,
      thetaOne: 0,
      iterations: 0
    }
  },

  created () {
    this.points.map(val =>
      console.log(val['x'] * 50, val['y'] / 10)
    )

    setInterval(this.learn, 500)
  },

  methods: {
    learn () {
      console.log('learn')
      let thetaZeroSum = 0
      let thetaOneSum = 0

      for (let i = 0; i < this.points.length; i++) {
        thetaZeroSum += this.hypothesis(this.points[i].x) - this.points[i].y
        thetaOneSum += (this.hypothesis(this.points[i].x) - this.points[i].y) * this.points[i].x
      }

      this.thetaZero = this.thetaZero - (this.learningRate / this.points.length) * thetaZeroSum
      this.thetaOne = this.thetaOne - (this.learningRate / this.points.length) * thetaOneSum

      this.iterations += 1
    },

    hypothesis (x) {
      return this.thetaZero + this.thetaOne * x
    }
  },

  render () {
    return (
      <div>
        <p>
          Iteration: {this.iteration}
        </p>
        <p>
          Hypothesis: f(x) = {this.thetaZero.toFixed(2)} {this.thetaOne.toFixed(2)}x
        </p>
        <svg style="border: 1px solid black" stroke="#000" stroke-width="1" width="650" height="650">
          {<line x1={0} y1={this.hypothesis(0)} x2={650} y2={this.hypothesis(-50)} stroke-width="2" stroke="black"/>}
          {this.points.map(val =>
            <circle cx={val['x'] * 50} cy={val['y'] / -10} stroke="#FF0000" fill="#FFF" stroke-width="3" r="5"/>
          )}
        </svg>
      </div>
    )
  }
}
