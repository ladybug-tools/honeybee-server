<template>
  <div class="panel panel-default">
    Job: {{job._id.$oid}} - {{job.created_by}}
    <div class="panel panel-default">
      <ul class="list-group">
        <li class="list-group-item" v-for="task in job.tasks">
          Task:
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        job: null
      }
    },
    methods: {
      getJob () {
        const path = `http://localhost:5000/api/job/` + this.$route.params.job_id
        axios.get(path)
          .then(response => {
            console.log(response);
            this.job = response.data
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    created () {
      this.getJob()
    }
  }
</script>
