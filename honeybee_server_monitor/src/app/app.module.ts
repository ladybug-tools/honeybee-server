import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { SimJobService } from './SimJob.service';
import { Http, HttpModule } from '@angular/http';
import { PopoverModule } from "ngx-popover";
import { Routes, RouterModule } from '@angular/router';
const routes: Routes = [
  {path: '',  component: AppComponent}
];
@NgModule({
  declarations: [
    AppComponent,

  ],
  imports: [
    BrowserModule,
    HttpModule,
    PopoverModule,
    FormsModule,
    RouterModule.forRoot(routes)
  ],
  providers: [SimJobService],
  bootstrap: [AppComponent]
})
export class AppModule { }
