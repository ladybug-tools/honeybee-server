<template>
  <div class="panel panel-default">
    <ul class="list-group">
      <li class="list-group-item"
          v-for="job in jobs">
        <router-link :to="'job/' + job.job_id">    
          Job: {{job.job_id}} - {{job.created_by}} - Status: {{ job.status }}
        </router-link>
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
      const path = `api/jobs`
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
