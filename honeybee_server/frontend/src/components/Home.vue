<template>
  <div class="panel panel-default">
    <ul class="list-group">
      <li class="list-group-item"
          v-for="job in jobs">
        <a v-bind:href="'/job/' + job.job_id">
          Job: {{job.job_id}} - {{job.created_by}} - Status: {{ job.status }}
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
      const path = `http://localhost:5000/api/jobs`
      axios.get(path)
        .then(response => {
          console.log(response.data)
          console.log(response.data.message)
          this.jobs = response.data.message
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
<style>
</style>
