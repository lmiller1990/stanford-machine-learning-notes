<template>
  <div id="app">
    <svg  width="100" height="100">
      <line x1="0" :y1="100 - hypothesis(0)" x2="100" :y2="100 - hypothesis(100)" stroke-width="2" stroke="black" />
      <circle v-for="d in DATA" :key="d[x]" :cx="d['squareMeter']" :cy="100 - d['price']"/>
    </svg>

    <p>
      Iteration: {{ iteration }}
    </p>
    <p>
      Hypothesis: f(x) = {{ thetaZero.toFixed(2) }} {{ thetaOne.toFixed(2) }}x
    </p>
    <p>
      Cost {{ cost.toFixed(2) }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      LEARNING_RATE: 0.0005, // learning rate
      thetaOne: 0,
      thetaZero: 0,
      M: 10, // total samples
      DATA: [],
      x: null,
      y: null,
      iteration: 0,
      interval: 0
    }
  },

  // start by creating some fake data. 
  created () {
    for (let i = 0; i < this.M; i++)
      this.DATA.push(this.createRandomTokyoHouse())

    this.x = this.DATA.map(data => data.squareMeter)
    this.y = this.DATA.map(data => data.price)
  },

  mounted () {
    // every 1ms, minimize slightly more.
    this.interval = setInterval(this.onLearn, 500)
  },
  
  computed: {
    cost () {
      // x is array of housing sizes
      // y is housing prices
      // M is size of training set
      let sum = 0

      for (let i = 0; i < this.M; i++) {
        sum += Math.pow(this.hypothesis(this.x[i]) - this.y[i],  2)
      }

      return sum / (2 * this.M)
    }
  },
  
  methods: {
    // helpers to generate some fake data
    getRandomIntFromInterval (min, max) {
      return Math.floor(Math.random() * (max - min + 1) + min)
    },

    createRandomTokyoHouse () {
      return {
        squareMeter: this.getRandomIntFromInterval(0, 100),
        price: this.getRandomIntFromInterval(0, 100),
      }
    },

    onLearn () {
      this.learn(this.LEARNING_RATE)
      this.iteration += 1 // keep track of the iterations
    },

    // exec until thetaZero and thetaOne converge.
    //  alpha is learning rate
    learn (alpha) {
      let thetaZeroSum = 0
      let thetaOneSum = 0

      for (let i = 0; i < this.M; i++) {
        thetaZeroSum += this.hypothesis(this.x[i]) - this.y[i]
        thetaOneSum += (this.hypothesis(this.x[i]) - this.y[i]) * this.x[i]
      }

      this.thetaZero = this.thetaZero - (alpha / this.M) * thetaZeroSum
      this.thetaOne = this.thetaOne - (alpha / this.M) * thetaOneSum
    },

    hypothesis (x) {
      return this.thetaZero + this.thetaOne * x
    }
  }
}
</script>

<style>
svg {
  background: #F3F3F3;
}

circle {
  fill: #FFFFFF;
  stroke: #FF0000;
  stroke-width: 3;
  r: 5;
}

line {
  stroke-width: 3;
  stroke: #000000;
}
</style>
