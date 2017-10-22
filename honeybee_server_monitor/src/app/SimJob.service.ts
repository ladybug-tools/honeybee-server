import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import * as _ from 'underscore';
import 'rxjs/add/operator/map';
import { SimJob } from './SimJob';
import { JobStatus } from './JobStatus.enum';

@Injectable()
export class SimJobService {

  data: any = null;
  simJob: SimJob;

  constructor(public http: Http) {
    this.simJob = new SimJob();
   }

  load(id) {
    if (this.data) {
      // already loaded data
      return Promise.resolve(this.data);
    }

    // var url = 'https://spreadsheets.google.com/feeds/cells/' + id + '/1/public/values?alt=json';
     var url = 'https://demo6383902.mockable.io/HBLive';
     url = id;
    

    // don't have the data yet
    return new Promise(resolve => {
      // We're using Angular Http provider to request the data,
      // then on the response it'll map the JSON data to a parsed JS object.
      // Next we process the data and resolve the promise with the new data.

      
      this.http.get(url)
        .map(res => {
          
        return res.json()
      })
      .subscribe((data) => {
        this.simJob = this.ConvertFromJson(data);
        this.simJob.Status = "Running"
        resolve(this.simJob);
        },
        (err) => {
          this.simJob.Status = "Error"
          return this.simJob;
        }
      );
      
    });
  }

  public ConvertFromJson(inJson) {
    let job = new SimJob();
    job.JobID = inJson.JobID;
    job.Simulations = _.toArray(inJson.Simulations);
    let finishedCounts = 0;
    job.StatusPercentage = 0;

    let simus = job.Simulations;
    // console.log(simus.length);

    simus.forEach((item) => {
      console.log(item.Status);
        if (item.Status === "done") {
            finishedCounts++;
        }
        
    })
    // console.log(finishedCounts);

    job.StatusPercentage = Math.round(finishedCounts / job.Simulations.length * 100);
     
    return job;
  }

}
