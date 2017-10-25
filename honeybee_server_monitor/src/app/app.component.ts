import { Component, OnInit } from '@angular/core';
import * as _ from 'underscore';
import { SimJobService } from './SimJob.service';
import { SimJob } from './SimJob';
import { ActivatedRoute,Router } from '@angular/router';
import 'rxjs/add/operator/filter';

// const appRoutes: Routes = [
//   { path: 'RunID', component: AppComponent },
//   { path: 'Inventory', component: AppInventory },
// ];

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],

})
export class AppComponent implements OnInit {
  
  serverURL: string;
  projects: any[]=[];
  info: Array<any>;
  dataId: string;
  title = 'app';
  JobStatusMsg: string;
  SimJob: SimJob;
  RunID: string;

  constructor(
    private simRun: SimJobService,
    private route: ActivatedRoute
    
  ) {
    this.SimJob = new SimJob();
    this.serverURL = "https://demo6383902.mockable.io/HBLive";
    this.JobStatusMsg = "";
  }

  ngOnInit(): void {
    this.route.queryParams
    .filter(params => params.RunID)
      .subscribe(params => {
        this.RunID = params.RunID;
        this.serverURL = params.RunID;
      console.log(params);
    });
  }

  CheckStatus() {
    // console.log(this.serverURL);
    
    this.simRun.load( this.serverURL )
    .then( ( data ) => {
      console.log(data);
      this.SimJob = data;
      // alert("Failed to connect the server2!")
      this.JobStatusMsg = this.SimJob.StatusPercentage.toString()+"%";
    }, (error) => {
      // console.log(error);
      alert("Failed to connect the server!")
    });
  }




}
