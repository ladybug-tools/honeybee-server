import { TestBed, inject } from '@angular/core/testing';

import { SimJobService } from './SimJob.service';

describe('JsonService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SimJobService]
    });
  });

  it('should be created', inject([SimJobService], (service: SimJobService) => {
    expect(service).toBeTruthy();
  }));
});
