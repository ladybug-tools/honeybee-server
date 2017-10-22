import * as _ from 'underscore';
import { Injectable } from '@angular/core';
import { SimChild } from './SimChild';
import { JobStatus } from './JobStatus.enum';


export class SimJob {
    JobID: string;
    Simulations: Array<SimChild>;
    Status: string;
    StatusPercentage: number;


    ConvertFromJson(inJson:any) {
        this.JobID = inJson.JobID
        this.Simulations = _.toArray(inJson.Simulations);
        
    }
}

