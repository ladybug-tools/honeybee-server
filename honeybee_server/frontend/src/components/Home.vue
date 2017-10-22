<template>
  <div class="panel panel-default">
    <ul class="list-group">
      <li class="list-group-item"
          v-for="job in jobs">
        <a v-bind:href="'/api/job/' + job._id.$oid">
          Job: {{job._id.$oid}} - {{job.created_by}}
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      jobs: null
    }
  },
  methods: {
    getJobs () {
      const path = `http://localhost:5000/api/job`
      axios.get(path)
        .then(response => {
          this.jobs = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getJobs()
  }
}
</script>
